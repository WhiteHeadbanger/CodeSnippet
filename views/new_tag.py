import flet as ft

from components import WHITE, CARD_SNIPPET_OPACITY, NAVBAR_SEARCH_OVERLAY_OPACITY, NAVBAR_SEARCH_TEXT_OPACITY, TAG_PURPLE, TAG_PINK, TAG_BLUE, TAG_GREEN
from components import Tag

class NewTagView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.colors = {
            'Purple': TAG_PURPLE,
            'Pink': TAG_PINK,
            'Blue': TAG_BLUE,
            'Green': TAG_GREEN
        }
        
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
                ft.dropdown.Option('Purple'),
                ft.dropdown.Option('Pink'),
                ft.dropdown.Option('Blue'),
                ft.dropdown.Option('Green'),
                
            ]
        )
        

    def build(self):
        self.content = ft.Container(
            width=400,
            height=600,
            alignment=ft.alignment.center,
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
                        on_click=lambda e: self.save_tag(e)
                    )
                ]
            )
        )

        return self.content

    def save_tag(self, e):
        self.route.page.go('/home')
        self.route.home.content.content.controls[1].controls[0].add_tag(Tag(60, 26, self.colors[self.color_dropdown.value], self.name_field.value))
        self.route.page.update()

    def close_view(self, e):
        self.route.page.go('/home')