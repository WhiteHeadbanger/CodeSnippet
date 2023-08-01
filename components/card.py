import flet as ft
from . import (
    CARD_SNIPPET_OPACITY,
    CARD_SNIPPET_TITLE_OPACITY,
    CARD_SNIPPET_DESCRIPTION_OPACITY,
    CARD_SNIPPET_DATE_OPACITY,
    WHITE
)

class Card(ft.UserControl):

    def __init__(self, width, height, title, *tags):
        super().__init__()
        self.width = width
        self.height = height
        self.title_text = title
        self.tags = [tag for tag in tags]

        self.title = ft.Text(
            value=self.title_text,
            size=17,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.with_opacity(CARD_SNIPPET_TITLE_OPACITY, WHITE)
        )
    
    def build(self):
        container = ft.Container(
            bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
            width=self.width,
            height=self.height,
            padding=10,
            content=ft.Column(
                controls=[
                    self.title,
                    ft.Row(
                        wrap=True
                    )
                ]
            )
        )

        for tag in self.tags:
            container.content.controls[1].controls.append(tag)
        
        return container
    
class CodeCard(Card):
    
    def __init__(self, width, height, title, date, description, *tags):
        super().__init__(width, height, title, *tags)
        self.date_text = date
        self.description_text = description

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
        container = super().build()

        container.content.controls.append(self.date)
        container.content.controls.append(self.description)
        
        return container
    
class TagCard(Card):

    def __init__(self, width, height, title, *tags):
        super().__init__(width, height, title, *tags)

    def build(self):
        container = super().build()

        new_tag_button = ft.TextButton(
            text="New tag"
        )
        container.content.controls.append(new_tag_button)
        return container