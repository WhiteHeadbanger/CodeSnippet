import flet as ft
from . import (
    CARD_SNIPPET_OPACITY,
    WHITE
)

class CodeEditor(ft.UserControl):

    def __init__(self):
        super().__init__()

        self.text_field = ft.TextField(
            hint_text="Your code...",
            bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
            color=WHITE,
            multiline=True,
            dense=False,
            on_change=self.handle_change,
            content_padding=5,
            focused_border_color=ft.colors.TRANSPARENT,
            #expand=True,
            prefix_text="1 ",
            min_lines=10
        )

    def build(self):
        return self.text_field

    def handle_change(self, e):
        ## Handle new lines
        count_new_lines = self.text_field.value.count("\n")
        
        self.text_field.prefix_text = "1 "  

        for i in range(1, count_new_lines+1):
            self.text_field.prefix_text += f'\n{i+1} '

        self.update()

    def clear_control(self):
        self.text_field.value = ""
        self.text_field.prefix_text = "1 "
        self.update()