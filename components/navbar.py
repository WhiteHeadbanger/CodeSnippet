import flet as ft
from . import (
    NAVBAR_BACKGROUND,
    NAVBAR_LOGO,
    NAVBAR_NEW_BACKGROUND_OPACITY,
    NAVBAR_NEW_TEXT_OPACITY,
    NAVBAR_SEARCH_OVERLAY_OPACITY,
    NAVBAR_SEARCH_TEXT_OPACITY,
    WHITE
)

from auth import SessionType

class NavBar(ft.UserControl):

    def __init__(self, route, session):
        super().__init__()
        self.route = route
        self.session = session

        self.login_required_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Not authenticated"),
            content=ft.Text("You must be logged in to create a new snippet."),
            actions=[
                ft.TextButton("Login", on_click=self.go_auth),
                ft.TextButton("Cancel", on_click=self.close_dialog)
            ]
        )

        self.login_button = ft.ElevatedButton(
                        text="Login",
                        bgcolor=ft.colors.with_opacity(NAVBAR_NEW_BACKGROUND_OPACITY, WHITE), 
                        color=ft.colors.with_opacity(NAVBAR_NEW_TEXT_OPACITY, WHITE),
                        on_click=self.go_auth,
                        visible=True
                    )
        
        self.logout_button = ft.ElevatedButton(
                        text="Logout",
                        bgcolor=ft.colors.with_opacity(NAVBAR_NEW_BACKGROUND_OPACITY, WHITE), 
                        color=ft.colors.with_opacity(NAVBAR_NEW_TEXT_OPACITY, WHITE),
                        on_click=self.go_logout,
                        visible=False
                    )
                    

    def build(self):
        self.container =  ft.Container(
            bgcolor=NAVBAR_BACKGROUND,
            content=ft.Row(
                height=70,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=50,
                controls=[
                    ft.Container(
                        on_click=self.go_home,
                        content=ft.Text(
                            value="Code Snippet",
                            color=NAVBAR_LOGO,
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        )
                    ),
                    ft.TextField(
                        width=600,
                        hint_text="Search",
                        bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE), 
                        color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
                        border=None,
                    ),
                    ft.ElevatedButton(
                        text="New",
                        bgcolor=ft.colors.with_opacity(NAVBAR_NEW_BACKGROUND_OPACITY, WHITE), 
                        color=ft.colors.with_opacity(NAVBAR_NEW_TEXT_OPACITY, WHITE),
                        on_click=self.go_newsnippet
                    ),
                    self.login_button,
                    self.logout_button
                ]
            )
        )
        
        return self.container
    
    def open_dialog(self):
        self.route.page.dialog = self.login_required_dialog
        self.login_required_dialog.open = True
        self.route.page.update()

    def close_dialog(self, e):
        self.login_required_dialog.open = False
        self.route.page.update()
    
    def go_newsnippet(self, e):
        if self.session.session_type == SessionType.USER: 
            self.route.page.go('/newsnippet')
        else:
            self.open_dialog()

    def go_auth(self, e):
        self.close_dialog(e)
        self.route.page.go('/auth')

    def go_logout(self, e):
        self.route.auth.logout()

    def go_home(self, e):
        self.route.page.go('/home')
    