import flet as ft
from components import TagCard, CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, NAVBAR_SEARCH_TEXT_OPACITY, WHITE

class EditSnippetView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.snippet_id = None

        self.code_editor = CodeEditor(self.route)
        self.tags_card = TagCard(self.route, 300, 500, "Your tags")
        self.snippet_tags = ft.Container(
            content=ft.Row(),
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            height=30,
        )
        self.title = ft.TextField(
            hint_text="Title",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
        )
        self.description = ft.TextField(
            hint_text="Description",
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            color=ft.colors.with_opacity(NAVBAR_SEARCH_TEXT_OPACITY, WHITE),
        )

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100),
            content=ft.ResponsiveRow(
                #vertical_alignment=ft.CrossAxisAlignment.START,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=40,
                controls=[
                    ft.Column(
                        width=1000,
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
                            ft.Row(controls=[self.tags_card, ft.IconButton(icon=ft.icons.CLOSE, on_click=self.go_home)], vertical_alignment=ft.CrossAxisAlignment.START),
                            #self.tags_card,
                            ft.TextButton(text="Save", on_click=self.save_snippet),
                        ]
                    ),
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.clear_controls()
        
        self.tags_card.clear_tags()
        for tag in self.route.home.tag_card.get_tags():
            t = Tag(self, 60, 26, tag.color, tag.text, False)
            self.tags_card.add_tag(t)
        
        existing_data = self.route.config.read_snippets_data()
        snippet = {}
        for snip in existing_data:
            if snip['id'] == self.snippet_id:
                snippet.update(snip)
        
        self.title.value = snippet['title']
        self.description.value = snippet['description']
        tags = [Tag(self, 60, 26, tag['color'], tag['text'], True) for tag in snippet['tags']]
        self.snippet_tags.content.controls = tags
        self.code_editor.text_field.value = snippet['code']
        self.code_editor.handle_on_change(None)

        self.update()

    def clear_controls(self):
        self.title.value = ""
        self.description.value = ""
        self.snippet_tags.content.controls.clear()
        self.code_editor.text_field.value = ""
        self.code_editor.text_field.prefix_text = "1 "
        self.code_editor.update()
        self.update()

    def save_snippet(self, e):
        existing_data = self.route.config.read_snippets_data()

        title = self.title.value
        description = self.description.value
        tags = [{"text":tag.text, "color":tag.color} for tag in self.snippet_tags.content.controls]
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
        for _tag in self.snippet_tags.content.controls:
            if _tag.color == tag.color and _tag.text == tag.text:
                self.delete_tag(_tag)
                return
        
        t = Tag(self, 60, 26, tag.color, tag.text, True)
        self.snippet_tags.content.controls.append(t)
        self.update()

    def delete_tag(self, tag):
        self.snippet_tags.content.controls.remove(tag)
        self.update()

    def go_home(self, e):
        self.route.page.go('/home')