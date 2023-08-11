import flet as ft
from components import CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE
from syntax_highlight.colors import COLORS


class SnippetView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.snippet_id = None

        self.title = ft.Text(size=24)
        self.description = ft.Text(size=20)
        self.tags = ft.Container(
            content=ft.Row(),
            height=30
        )
        self.code_area = ft.Container(
            width=700,
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            content=ft.Column()
        )

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
                    self.code_area
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
        tags = [Tag(self, 60, 26, tag['color'], tag['text']) for tag in snippet['tags']]
        self.tags.content.controls = tags
        
        # iterate over tokenized code
        row_counter = 0
        self.code_area.content.controls.append(ft.Row())
        self.code_area.content.controls[0].controls.append(ft.Text("1 "))
        for token in snippet['tokens']:
            if token[0] in ['NEWLINE', 'NL']:
                row_counter += 1
                self.code_area.content.controls.append(ft.Row())
                self.code_area.content.controls[row_counter].controls.append(ft.Text(f"{row_counter+1}"))
                continue

            elif token[0] == 'INDENT':
                self.code_area.content.controls[row_counter].controls[0].spans.append(ft.TextSpan(text="    "))
                continue
            elif token[0] == 'SPACE':
                self.code_area.content.controls[row_counter].controls[0].spans.append(ft.TextSpan(text=" "))
                continue
            elif token[0] == 'ENDMARKER':
                continue

            else:
                self.code_area.content.controls[row_counter].controls[0].spans.append(ft.TextSpan(text=token[1], style=ft.TextStyle(color=COLORS[token[0]])))
        
        self.update()

    def update_code(self, code):
        pass

    def clear_controls(self):
        self.title.value = ""
        self.description.value = ""
        self.tags.content.controls.clear()
        self.code_area.content.controls.clear()
        self.update()
