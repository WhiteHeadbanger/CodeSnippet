import flet as ft
from . import (
    CARD_SNIPPET_OPACITY,
    WHITE
)

class CodeEditor(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        
        self.line_counter = 1

        self.prefix_control = ft.ListView([ft.Text("1")])

        self.text_field = ft.TextField(
            bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
            width=500,
            color=WHITE,
            multiline=True,
            dense=False,
            on_change=self.handle_on_change,
            expand=True,
            #prefix=self.prefix_control,
            prefix_text=str(self.line_counter),
            content_padding=5
        )

    def build(self):
        self.container = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.text_field]
            )
        )

        return self.container

    def handle_on_change(self, e):
        count_new_lines = self.text_field.value.count("\n")
        
        self.text_field.prefix_text = "1"
        if count_new_lines == 0:
            self.update()
            return
        
        self.text_field.prefix_text = "1"
        for i in range(1, count_new_lines):
            self.text_field.prefix_text += f'\n{i+1}'
        self.text_field.prefix_text += f'\n{count_new_lines+1}'

        self.update()