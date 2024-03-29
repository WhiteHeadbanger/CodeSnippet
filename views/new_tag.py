import flet as ft

from components import WHITE, CARD_SNIPPET_OPACITY, NAVBAR_SEARCH_OVERLAY_OPACITY, NAVBAR_SEARCH_TEXT_OPACITY, TAG_PURPLE, TAG_PINK, TAG_BLUE, TAG_GREEN
from components import TagDataclass
from uuid import uuid4

class NewTagView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.initialized = False
        self.colors = {
            'Purple': TAG_PURPLE,
            'Pink': TAG_PINK,
            'Blue': TAG_BLUE,
            'Green': TAG_GREEN
        }
        
        self.name_field = ft.TextField(
            hint_text="Name",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_bgcolor=ft.colors.with_opacity(0.1, WHITE),
            border_color=ft.colors.TRANSPARENT,
            focused_border_color=ft.colors.TRANSPARENT
        )
        
        self.color_dropdown = ft.Dropdown(
            label="Color",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_bgcolor=ft.colors.with_opacity(0.1, WHITE),
            border_color=ft.colors.TRANSPARENT,
            focused_border_color=ft.colors.TRANSPARENT,
            options=[
                ft.dropdown.Option('Purple'),
                ft.dropdown.Option('Pink'),
                ft.dropdown.Option('Blue'),
                ft.dropdown.Option('Green'),
                
            ]
        )
        
    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100),
            width=400,
            height=600,
            alignment=ft.alignment.center,
            padding=10,
            bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Row(
                        controls=[ft.Text("New Tag", size=20), ft.IconButton(icon=ft.icons.CLOSE, on_click=self.close_view)],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    self.name_field,
                    self.color_dropdown,
                    ft.FilledButton(
                        text="Save",
                        on_click=self.create_tag,
                    ),
                ]
            )
        )

        return self.content
    
    def initialize(self):
        pass
    
    def create_tag(self, e):
        tag = TagDataclass(id = str(uuid4()), color = self.colors[self.color_dropdown.value], text = self.name_field.value)
        self.route.config.save_tags_data(tag)
        self.route.page.go('/home')

    def close_view(self, e):
        self.route.page.go('/home')