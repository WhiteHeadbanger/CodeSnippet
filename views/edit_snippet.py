import flet as ft
from components import CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, NAVBAR_SEARCH_TEXT_OPACITY, WHITE

class EditSnippetView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.snippet_id = None

        
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
            content=ft.Row(),
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            height=30,
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
                        width=1000,
                        col=6,
                        controls=[
                            self.title,
                            self.description,
                            self.tags_text_field,
                            self.snippet_tags,
                            self.code_editor
                        ]
                    ),
                    ft.Column(
                        col=2,
                        controls=[
                            ft.IconButton(icon=ft.icons.CLOSE, on_click=self.go_home),
                            ft.TextButton(text="Save", on_click=self.save_snippet),
                        ]
                    ),
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.clear_controls()
        
        existing_data = self.route.config.read_snippets_data()
        snippet = {}
        for snip in existing_data:
            if snip['id'] == self.snippet_id:
                snippet.update(snip)
        
        self.title.value = snippet['title']
        self.description.value = snippet['description']
        tags = [Tag(self, tag['text']) for tag in snippet['tags']]
        self.snippet_tags.content.controls = tags
        self.code_editor.text_field.value = snippet['code']
        self.code_editor.handle_change(None)

        self.update()

    def clear_controls(self):
        self.title.value = ""
        self.description.value = ""
        self.tags_text_field.value = ""
        self.snippet_tags.content.controls.clear()
        self.code_editor.clear_control()
        self.update()

    def save_snippet(self, e):
        existing_data = self.route.config.read_snippets_data()

        title = self.title.value
        description = self.description.value
        tags = [{"text":tag.text} for tag in self.snippet_tags.content.controls]
        code = self.code_editor.text_field.value
        for snip in existing_data:
            if snip['id'] == self.snippet_id:
                snip['title'] = title
                snip['description'] = description
                snip['tags'] = tags
                snip['code'] = code

        self.route.config.save_snippets_data(existing_data)
        self.route.page.go('/home')
        self.route.page.update()

    def add_tag(self, tag):
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

    def go_home(self, e):
        self.clear_controls()
        self.route.page.go('/home')