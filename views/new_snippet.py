import flet as ft
from components import TagCard, CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE, NAVBAR_SEARCH_TEXT_OPACITY

class NewSnippetView(ft.UserControl):
    
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.code_editor = CodeEditor(self.route)
        self.tags_card = TagCard(self.route, 300, 500, "Your tags")
        self.snippet_tags = ft.Container(
            content=ft.Row(),
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            height=30,
        )

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100, left=270),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=40,
                controls=[
                    ft.Column(
                        width=1000,
                        controls=[
                            ft.TextField(
                                hint_text="Title",
                                bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
                                color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
                            ),
                            ft.TextField(
                                hint_text="Description",
                                bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
                                color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
                            ),
                            ft.Text("Selected tags:"),
                            self.snippet_tags,
                            self.code_editor
                        ]
                    ),
                    ft.Column(
                        controls=[
                            self.tags_card,
                            ft.TextButton(text="Save", on_click=self.save_snippet),
                        ]
                    ),
                    ft.IconButton(icon=ft.icons.CLOSE, on_click=self.go_home)
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.tags_card.clear_tags()
        for tag in self.route.home.tag_card.get_tags():
            t = Tag(self.route, 60, 26, tag.color, tag.text, 'new_tag')
            self.tags_card.add_tag(t)
        
        self.update()

    def save_snippet(self, e):
        pass

    def go_home(self, e):
        self.route.page.go('/home')

    def add_tag(self, tag):
        if tag in self.snippet_tags.content.controls:
            self.snippet_tags.content.controls.remove(tag)
            self.update()
            return
        
        t = Tag(self.route, 60, 26, tag.bgcolor, tag.content.value, 'new_tag')
        self.snippet_tags.content.controls.append(t)
        self.update()
    

