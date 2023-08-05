import flet as ft
from . import WHITE

class Tag(ft.UserControl):

    def __init__(self, route, width, height, color, text, section):
        super().__init__()
        self.route = route
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.section = section

    def build(self):
        self.content = ft.Container(
            bgcolor=self.color,
            width=self.width,
            height=self.height,
            padding=5,
            border_radius=20,
            on_click=self.handle_on_click,
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
        if self.section == 'home':
            pass
        elif self.section == 'new_tag':
            self.route.new_snippet.add_tag(self.content)