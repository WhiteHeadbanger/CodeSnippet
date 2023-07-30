import flet as ft
from . import WHITE

class Tag(ft.UserControl):

    def __init__(self, width, height, color, text):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.text = text

    def build(self):
        return ft.Container(
            bgcolor=self.color,
            width=self.width,
            height=self.height,
            padding=5,
            border_radius=20,
            content=ft.Text(
                value=self.text,
                weight=ft.FontWeight.BOLD,
                size=11,
                color=WHITE,
                text_align=ft.TextAlign.CENTER,

            )
        )