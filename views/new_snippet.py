import flet as ft
from syntax_highlight.utils import save_code_to_file, delete_code_file
from syntax_highlight.lexers.python import tokenizer
from components import TagCard, CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE, NAVBAR_SEARCH_TEXT_OPACITY
from uuid import uuid4
from constants import TAG_WIDTH, TAG_HEIGHT

class NewSnippetView(ft.UserControl):
    
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.code_editor = CodeEditor(self)
        self.tags_card = TagCard(self, width=300, title="Your tags")
        self.tags_card.new_tag_button.visible = False
        self.snippet_tags = ft.Container(
            content=ft.Row(),
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            height=30,
            width=700,
        )
        self.title = ft.TextField(
            width=700,
            hint_text="Title",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )
        self.description = ft.TextField(
            width=700,
            hint_text="Description",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )


    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100),
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=40,
                controls=[
                    ft.Column(
                        col=6,
                        controls=[
                            self.title,
                            self.description,
                            ft.Text("Selected tags:"),
                            self.snippet_tags,
                            self.code_editor
                        ]
                    ),
                    ft.Column(
                        col=2,
                        controls=[
                            ft.Row(
                                vertical_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    self.tags_card 
                                ], 
                            ),
                            ft.Row(
                                vertical_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    ft.TextButton(text="Save", on_click=self.save_snippet),
                                    ft.TextButton(text="Close", on_click=self.go_home)
                                ]
                            )
                        ]
                    ),
                    
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.clear_controls()
        for tag in self.route.home.tag_card.get_tags():
            t = Tag(self, TAG_WIDTH, TAG_HEIGHT, tag.color, tag.text, False)
            self.tags_card.add_tag(t)
        
        self.update()

    def clear_controls(self):
        self.tags_card.clear_tags()
        self.title.value = ""
        self.description.value = ""
        self.code_editor.clear_control()
        self.update()

    def get_control_data(self):
        id = str(uuid4())
        title = self.title.value
        description = self.description.value
        tags = [{"text":tag.text, "color":tag.color} for tag in self.snippet_tags.content.controls]
        code = self.code_editor.text_field.value
        
        return id, title, description, tags, code

    def save_snippet(self, e):
        existing_data = self.route.config.read_snippets_data()
        
        id, title, description, tags, code = self.get_control_data()

        #save code to temp file
        save_code_to_file(code)
        #tokenize
        tokens = tokenizer()
        # delete file
        delete_code_file()

        data = {
            'id': id,
            'title': title,
            'description': description,
            'tags': tags,
            'date': 'now',
            'code': code,
            'tokens': tokens
        }
        existing_data.append(data)
        self.route.config.save_snippets_data(existing_data)

        self.route.page.go('/home')
        self.route.page.update()

    def go_home(self, e):
        # clear controls and go home
        self.clear_controls()
        self.route.page.go('/home')

    def add_tag(self, tag):
        for _tag in self.snippet_tags.content.controls:
            if _tag.color == tag.color and _tag.text == tag.text:
                self.delete_tag(_tag)
                return
        
        t = Tag(self, TAG_WIDTH, TAG_HEIGHT, tag.color, tag.text, True)
        self.snippet_tags.content.controls.append(t)
        self.update()

    def delete_tag(self, tag):
        self.snippet_tags.content.controls.remove(tag)
        self.update()

    def clear_controls(self):
        self.title.value = ""
        self.description.value = ""
        self.snippet_tags.content.controls.clear()
        self.code_editor.clear_control()
    

