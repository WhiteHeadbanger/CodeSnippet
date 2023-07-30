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

class NavBar(ft.UserControl):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def build(self):
        return ft.Container(
            bgcolor=NAVBAR_BACKGROUND,
            content=ft.Row(
                width=self.width,
                height=self.height,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=50,
                controls=[
                    ft.Text(
                        value="Code Snippet", 
                        color=NAVBAR_LOGO,
                        size=20,
                        weight=ft.FontWeight.BOLD,
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
                        color=ft.colors.with_opacity(NAVBAR_NEW_TEXT_OPACITY, WHITE)
                    )
                ]
            )
        )
    