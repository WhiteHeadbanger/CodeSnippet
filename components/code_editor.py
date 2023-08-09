import flet as ft
from . import (
    CARD_SNIPPET_OPACITY,
    WHITE
)

class CodeEditor(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route

        self.text_field = ft.TextField(
            hint_text="Your code...",
            width=700,
            bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
            color=WHITE,
            multiline=True,
            dense=False,
            on_change=self.handle_on_change,
            prefix_text="1 ",
            content_padding=5,
            focused_border_color=ft.colors.TRANSPARENT
        )

    def build(self):
        self.container = ft.Container(
            content=ft.Row(
                controls=[self.text_field],
            )
        )

        return self.container

    def handle_on_change(self, e):
        count_new_lines = self.text_field.value.count("\n")
        
        self.text_field.prefix_text = "1 "
        if count_new_lines == 0:
            self.update()
            return
        
        for i in range(1, count_new_lines):
            self.text_field.prefix_text += f'\n{i+1} '
        self.text_field.prefix_text += f'\n{count_new_lines+1} '

        self.update()