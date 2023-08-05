import flet as ft
from components import CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE, NAVBAR_SEARCH_TEXT_OPACITY, BODY_OPACITY

class SnippetView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.snippet_id = None

        self.title = ft.Text(size=24)
        self.description = ft.Text(size=20)
        self.tags = ft.Container(
            content=ft.Row(),
            #bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            height=30
        )
        self.code_editor = CodeEditor(self.route)

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100, left=270),
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            padding=10,
            width=1000,
            content=ft.Column(
                spacing=10,
                controls=[
                    self.title,
                    self.description,
                    self.tags,
                    self.code_editor
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.clear_controls()
        existing_data = self.route.config.read_data()
        snippet = {}
        for snip in existing_data:
            if snip['id'] == self.snippet_id:
                snippet.update(snip)
        
        self.title.value = snippet['title']
        self.description.value = snippet['description']
        tags = [Tag(self.route, 60, 26, tag['color'], tag['text'], 'snippet') for tag in snippet['tags']]
        self.tags.content.controls = tags
        self.code_editor.text_field.value = snippet['code']
        self.code_editor.handle_on_change(None)
        self.code_editor.text_field.disabled = True
        self.code_editor.update()
        self.update()

    def clear_controls(self):
        self.title.value = ""
        self.description.value = ""
        self.tags.content.controls.clear()
        self.code_editor.text_field.value = ""
        self.code_editor.text_field.prefix_text = "1 "
        self.code_editor.update()
        self.update()
