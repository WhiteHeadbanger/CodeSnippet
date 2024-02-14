import flet as ft
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE, NAVBAR_SEARCH_TEXT_OPACITY
from auth import User, SessionType
from uuid import uuid4

class AuthView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route

        self.username_field = ft.TextField(   
            hint_text="Username",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )
        self.password_field = ft.TextField(
            hint_text="Password",
            password=True,
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )
        self.confirm_password_field = ft.TextField(
            hint_text="Confirm Password",
            password=True,
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )
        self.email_field = ft.TextField(
            hint_text="Email",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )
        self.login_button = ft.TextButton("Login", on_click=self.login)
        self.sign_up_button = ft.TextButton("Sign Up", on_click=self.sign_up)

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100),
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=40,
                controls=[
                    ft.Column(
                        col=6,
                        controls=[
                            self.username_field,
                            self.password_field,
                            self.login_button,
                            ft.Text(spans=[ft.TextSpan(text="Forgot Password?", on_click=self.load_forgot_password_view)]),
                            ft.Text(spans=[ft.TextSpan(text="Sign Up", on_click=self.load_sign_up_view)])
                        ],
                    )
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.clear_controls()
        self.update()

    def clear_controls(self):
        self.username_field.value = ""
        self.username_field.error_text = None
        self.password_field.value = ""
        self.password_field.error_text = None
        self.confirm_password_field.value = ""
        self.confirm_password_field.error_text = None
        self.email_field.value = ""
        self.email_field.error_text = None
        self.update()
    
    def load_forgot_password_view(self, e):
        controls = self.content.content.controls[0].controls
        controls.clear()
        controls.append(self.email_field)
        controls.append(ft.TextButton("Submit", on_click=self.send_email))
        controls.append(ft.Text(spans=[ft.TextSpan(text="Cancel", on_click=self.load_login_view)]))
        self.content.content.controls[0].controls = controls
        self.update()

    def load_sign_up_view(self, e):
        controls = self.content.content.controls[0].controls 
        controls.clear()
        controls.append(self.username_field)
        controls.append(self.password_field)
        controls.append(self.confirm_password_field)
        controls.append(self.email_field)
        controls.append(self.sign_up_button)
        controls.append(ft.Text(spans=[ft.TextSpan(text="Have an account? Login instead", on_click=self.load_login_view)]))
        self.content.content.controls[0].controls = controls
        self.update()

    def load_login_view(self, e):
        controls = self.content.content.controls[0].controls
        controls.clear()
        controls.append(self.username_field)
        controls.append(self.password_field)
        controls.append(self.login_button)
        controls.append(ft.Text(spans=[ft.TextSpan(text="Forgot Password?", on_click=self.load_forgot_password_view)]))
        controls.append(ft.Text(spans=[ft.TextSpan(text="Sign Up", on_click=self.load_sign_up_view)]))
        self.content.content.controls[0].controls = controls
        self.update()

    def send_email(self, e):
        pass

    def sign_up(self, e):
        username = self.username_field.value if self.username_field.value != "" else None
        password = self.password_field.value if (self.password_field.value == self.confirm_password_field.value) and self.password_field.value != "" else None
        email = self.email_field.value if self.email_field.value != "" else None
        if username is None:
            self.username_field.error_text = "Username cannot be empty"
        elif password is None:
            self.password_field.error_text = "Passwords don't match"
        elif email is None:
            self.email_field.error_text = "Email cannot be empty"
        else:
            user = User(id=str(uuid4()), username=username, password=password, email=email)
            self.route.config.save_user_data(user)
            self.clear_controls()
            self.load_login_view(e)

        self.update()

    def login(self, e):
        username = self.username_field.value if self.username_field.value != "" else None
        password = self.password_field.value if self.password_field.value != "" else None
        if username is None:
            self.username_field.error_text = "Username cannot be empty"
        elif password is None:
            self.password_field.error_text = "Password cannot be empty"
        else:
            user = self.route.config.get_user_data(username)
            if user is None:
                self.username_field.error_text = "User not found"
            elif user['password'] != password:
                self.password_field.error_text = "Password is incorrect"
            else:
                self.route.session.session_type = SessionType.USER
                self.clear_controls()
                self.route.navbar.logout_button.visible = True
                self.route.navbar.login_button.visible = False
                self.route.navbar.update()
                self.route.page.go('/home')
                return

        self.update()

    def logout(self):
        self.route.session.session_type = SessionType.ANON
        self.route.navbar.logout_button.visible = False
        self.route.navbar.login_button.visible = True
        self.route.navbar.update()
        self.route.page.go('/home')
        
