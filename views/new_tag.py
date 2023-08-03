import flet as ft
from . import BaseView
from components import WHITE, CARD_SNIPPET_OPACITY, NAVBAR_SEARCH_OVERLAY_OPACITY, NAVBAR_SEARCH_TEXT_OPACITY

class NewTagView(BaseView):

    def __init__(self, page, *args, **kwargs):
        super().__init__(page, *args, **kwargs)
        self.route = '/newtag'
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.name_field = ft.TextField(
            hint_text="Name",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE)
        )
        self.color_dropdown = ft.Dropdown(
            label="Color",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            options=[
                ft.dropdown.Option('purple'),
                ft.dropdown.Option('pink'),
                ft.dropdown.Option('blue'),
                ft.dropdown.Option('green'),
                
            ]
        )
        self.controls = [
            ft.Container(
                width=400,
                height=600,
                bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[ft.IconButton(icon=ft.icons.CLOSE, on_click=lambda e: self.close_view(e))],
                            alignment=ft.MainAxisAlignment.END
                        ),
                        self.name_field,
                        self.color_dropdown,
                        ft.TextButton(
                            text="Save",
                            on_click=lambda e: self.handle_click(e)
                        )
                    ]
                )
            )
        ]

    def handle_click(self, e):
        self.page.client_storage.set(key='tag', value=(self.name_field.value, self.color_dropdown.value))
        e.page.go('/home')

    def close_view(self, e):
        e.page.go('/home')

def _newtag_view_(page):
    return NewTagView(page)