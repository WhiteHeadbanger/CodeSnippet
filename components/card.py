import flet as ft
from . import (
    CARD_SNIPPET_OPACITY,
    CARD_SNIPPET_TITLE_OPACITY,
    CARD_SNIPPET_DESCRIPTION_OPACITY,
    CARD_SNIPPET_DATE_OPACITY,
    WHITE
)

class Card(ft.UserControl):

    def __init__(self, route, width, height, title, tags = None):
        super().__init__()
        self.route = route
        self.width = width
        self.height = height
        self.title_text = title
        self.tags = [tag for tag in tags] if tags is not None else []

        self.title = ft.Text(
            value=self.title_text,
            size=17,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.with_opacity(CARD_SNIPPET_TITLE_OPACITY, WHITE)
        )

        self.tag_row = ft.Row(wrap=True)
    
    def build(self):
        self.container = ft.Container(
            bgcolor=ft.colors.with_opacity(CARD_SNIPPET_OPACITY, WHITE),
            width=self.width,
            height=self.height,
            padding=10,
            content=ft.Column(
                controls=[
                    self.title,
                    self.tag_row
                ]
            )
        )

        for tag in self.tags:
            self.container.content.controls[1].controls.append(tag)
        
        return self.container
    
    def add_tag(self, tag):
        self.tag_row.controls.append(tag)
        self.update()

    def get_tags(self):
        return self.tag_row.controls
    
    def clear_tags(self):
        self.tag_row.controls.clear()
        self.update()
    
class CodeCard(Card):
    
    def __init__(self, route, width, height, title, date, description, tags = None, code = None):
        super().__init__(route, width, height, title, tags)
        self.date_text = date
        self.description_text = description
        self.code = code
        self.hovered = False

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
        self.container = super().build()
        self.container.scale = ft.transform.Scale(1)
        self.container.animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
        #self.container.on_click = lambda e: self.handle_click(e)
        self.container.on_hover = lambda e: self.handle_hover(e)

        self.container.content.controls.append(self.date)
        self.container.content.controls.append(self.description)
        
        return self.container
    
    def handle_click(self, e):
        e.page.go('/snippet')

    def handle_hover(self, e):
        if not self.hovered:
            self.hovered = True
            self.animate_hovered()
            self.update()
        
        elif self.hovered:
            self.hovered = False
            self.animate_unhovered()
            self.update()
    
    def animate_hovered(self):
        self.container.scale = 1.1
    
    def animate_unhovered(self):
        self.container.scale = 1
    
class TagCard(Card):

    def __init__(self, route, width, height, title, tags = None):
        super().__init__(route, width, height, title, tags)

    def build(self):
        self.container = super().build()

        new_tag_button = ft.TextButton(
            text="New tag",
            on_click=self.go_newtag
        )
        self.container.content.controls.append(new_tag_button)
        return self.container

    def go_newtag(self, e):
        self.route.page.go('/newtag')
