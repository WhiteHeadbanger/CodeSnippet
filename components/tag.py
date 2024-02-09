import flet as ft
from dataclasses import dataclass
from . import WHITE

@dataclass
class TagDataclass:
    id: str
    text: str

class Tag(ft.UserControl):

    def __init__(self, route, text):
        super().__init__()
        self.route = route
        self.text = text
        self.hovered = False

        self.text_control = ft.Text(
                value=self.text,
                weight=ft.FontWeight.BOLD,
                size=11,
                color=WHITE,
                text_align=ft.TextAlign.CENTER,
                no_wrap=True
            )

        self.delete_control = ft.IconButton(
            icon=ft.icons.DELETE,
            icon_color=WHITE,
            icon_size=14
        )

        self.content = ft.Container(
            bgcolor='#1a1919',
            height=26,
            padding=5,
            on_click=self.remove_tag,
            on_hover=self.handle_hover,
            content=self.text_control,
        )

    def build(self):
        return self.content
    
    def remove_tag(self, e):
        self.route.snippet_tags.content.controls.remove(self)
        self.route.update()

    def handle_hover(self, e):
        if not self.hovered:
            self.hovered = True
            self.content.bgcolor = '#ad0707'
            self.content.content = self.delete_control
            self.content.padding = 0
            self.content.width = 100
            self.update()
        else:
            self.hovered = False
            self.content.bgcolor = '#1a1919'
            self.content.content = self.text_control
            self.content.padding = 5
            self.content.width = None
            self.update()