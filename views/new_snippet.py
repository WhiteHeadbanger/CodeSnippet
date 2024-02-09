import flet as ft
from syntax_highlight.utils import save_code_to_file, delete_code_file
from syntax_highlight.lexers.python import tokenizer
from components import CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE, NAVBAR_SEARCH_TEXT_OPACITY
from uuid import uuid4

class NewSnippetView(ft.UserControl):
    
    def __init__(self, route):
        super().__init__()
        self.route = route
        
        self.title = ft.TextField(
            hint_text="Title",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )
        self.description = ft.TextField(
            hint_text="Description",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT
        )
        self.tags_text_field = ft.TextField(
            hint_text="Tags",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
            focused_border_color=ft.colors.TRANSPARENT,
            on_submit=self.add_tag,
        )
        self.snippet_tags = ft.Container(
            content=ft.Row(wrap=True, run_spacing=10),
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            height=26
        )
        self.code_editor = CodeEditor()


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
                            self.tags_text_field,
                            self.snippet_tags,
                            self.code_editor
                        ],
                    ),
                    ft.Column(
                        col=2,
                        controls=[
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
        self.update()

    def clear_controls(self):
        self.title.value = ""
        self.description.value = ""
        self.tags_text_field.value = ""
        self.snippet_tags.content.controls.clear()
        self.code_editor.clear_control()
        self.update()

    def get_control_data(self):
        id = str(uuid4())
        title = self.title.value
        description = self.description.value
        tags = [{"text":tag.text} for tag in self.snippet_tags.content.controls]
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

    def add_tag(self, e):
        new_tag_text = self.tags_text_field.value
        
        # Validations
        if new_tag_text == "":
            return
        elif new_tag_text in [tag.text for tag in self.snippet_tags.content.controls]:
            return
        else:
            # Create new tag and add it to the snippet tags
            new_tag = Tag(self, new_tag_text)
            self.snippet_tags.content.controls.append(new_tag)

        # Clear text field and focus it
        self.tags_text_field.value = ""
        self.tags_text_field.focus()

        self.update()

    def delete_tag(self, tag):
        self.snippet_tags.content.controls.remove(tag)
        self.update()
    

