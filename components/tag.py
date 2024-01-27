import flet as ft
from dataclasses import dataclass
from . import WHITE

@dataclass
class TagDataclass:
    id: str
    color: str
    text: str

class Tag(ft.UserControl):

    def __init__(self, route, width, height, color, text, selected: bool | None = None):
        super().__init__()
        self.route = route
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.selected = selected

    def build(self):
        self.content = ft.Container(
            bgcolor=self.color,
            width=self.width,
            height=self.height,
            padding=5,
            border_radius=20,
            on_click=self.handle_on_click if self.selected is not None else None,
            content=ft.Text(
                value=self.text,
                weight=ft.FontWeight.BOLD,
                size=11,
                color=WHITE,
                text_align=ft.TextAlign.CENTER,

            )
        )

        return self.content
    
    def handle_on_click(self, e):
        if self.selected:
            self.route.delete_tag(self)
        else:
            self.route.add_tag(self)