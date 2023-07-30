import flet as ft
from . import (
    CARD_SNIPPET_OPACITY,
    CARD_SNIPPET_TITLE_OPACITY,
    CARD_SNIPPET_DESCRIPTION_OPACITY,
    CARD_SNIPPET_DATE_OPACITY,
    WHITE
)

class CodeCard(ft.UserControl):
    
    def __init__(self, width, height, title, date, description, *tags):
        super().__init__()
        self.width = width
        self.height = height
        self.title_text = title
        self.date_text = date
        self.description_text = description
        self.tags = [tag for tag in tags]

        self.title = ft.Text(
            value=self.title_text,
            size=17,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.with_opacity(CARD_SNIPPET_TITLE_OPACITY, WHITE)
        )

        self.date = ft.Text(
            value=self.date_text,
            size=12,
            weight=ft.FontWeight.W_100,
            color=ft.colors.with_opacity(CARD_SNIPPET_DATE_OPACITY, WHITE)
        )

        self.description = ft.Text(
            value=self.description_text,
            size=15,
            weight=ft.FontWeight.NORMAL,
            color=ft.colors.with_opacity(CARD_SNIPPET_DESCRIPTION_OPACITY, WHITE)
        )

    def build(self):
        container =  ft.Container(
            bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
            width=self.width,
            height=self.height,
            padding=10,
            content=ft.Column(
                controls=[
                    self.title,
                    ft.Row(
                        controls=[]
                    )
                ]
            )
        )

        for tag in self.tags:
            container.content.controls[1].controls.append(tag)

        container.content.controls.append(self.date)
        container.content.controls.append(self.description)
        
        return container