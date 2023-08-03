import flet as ft
from components import TagCard
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE, NAVBAR_SEARCH_TEXT_OPACITY

class NewSnippetView(ft.UserControl):
    
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.tags_card = TagCard(self.route, 300, 500, "Your tags")

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100, left=270),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=40,
                controls=[
                    ft.Column(
                        width=1000,
                        controls=[
                            ft.TextField(
                                hint_text="Title",
                                bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
                                color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
                            ),
                            ft.TextField(
                                hint_text="Description",
                                bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
                                color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
                            ),
                            ft.TextField(
                                hint_text="Language",
                                bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
                                color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
                            ),
                            ft.TextField(
                                bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
                                color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
                                height=800,
                                multiline=True,
                                dense=False
                            )
                        ]
                    ),
                    ft.Column(
                        controls=[
                            self.tags_card,
                            ft.TextButton(text="Save", on_click=self.save_snippet),
                        ]
                    )
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.update()

    def save_snippet(self, e):
        pass

    

