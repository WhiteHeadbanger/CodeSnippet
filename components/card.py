import copy
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
        self.tags = tags if tags is not None else []

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
            self.tag_row.controls.append(tag)
        
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
    
    def __init__(self, id, route, width, height, title, date, description, tags = None, code = None):
        super().__init__(route, width, height, title, tags)
        self.id = id
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

        self.edit_button = ft.IconButton(
            icon=ft.icons.EDIT,
            on_click=self.go_edit_snippet,
            visible=False,
            icon_size=17
        )

        self.delete_button = ft.IconButton(
            icon=ft.icons.DELETE,
            on_click=self.go_delete_snippet,
            visible=False,
            icon_size=17,
            icon_color=ft.colors.RED_ACCENT
        )

    def build(self):
        self.container = super().build()
        self.container.scale = ft.transform.Scale(1)
        self.container.animate_scale=ft.animation.Animation(600, ft.AnimationCurve.EASE)
        self.container.on_click = self.handle_click
        self.container.on_hover = self.handle_hover

        self.container.content.controls.remove(self.title)
        self.container.content.controls.insert(0, (ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.title,
                ft.Row(
                    spacing=10,
                    controls=[
                        self.edit_button, 
                        self.delete_button
                    ]
                ) 
            ]
        )))
        self.container.content.controls.append(self.date)
        self.container.content.controls.append(self.description)

        return self.container
    
    def handle_click(self, e):
        self.route.snippet.snippet_id = self.id
        self.route.page.go('/snippet')

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
        self.edit_button.visible = True
        self.delete_button.visible = True
    
    def animate_unhovered(self):
        self.container.scale = 1
        self.edit_button.visible = False
        self.delete_button.visible = False

    def go_edit_snippet(self, e):
        self.route.edit_snippet.snippet_id = self.id
        self.route.page.go('/editsnippet')

    def go_delete_snippet(self, e):
        self.route.home.open_dialog(self)
        
    
class TagCard(Card):

    def __init__(self, route, width, height, title, tags = None):
        super().__init__(route, width, height, title, tags)

        self.new_tag_button = ft.TextButton(
            text="New tag",
            on_click=self.go_newtag
        )

    def build(self):
        self.container = super().build()
        self.container.content.controls.append(self.new_tag_button)
        return self.container

    def go_newtag(self, e):
        self.route.page.go('/newtag')
