import flet as ft
from components import CodeEditor, Tag
from components import NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE
from syntax_highlight.colors import COLORS

import pyperclip

class SnippetView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        self.snippet_id = None

        self.title = ft.Text(size=30)
        self.description = ft.Text(size=20)
        self.copy_code_button = ft.IconButton(
            icon=ft.icons.COPY,
            on_click=self.copy_code_to_clipboard,
            visible=True,
            icon_size=17
        )
        self.tags = ft.Container(
            content=ft.Row(),
            height=30
        )
        self.code_area = ft.Container(
            width=700,
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            content=ft.Column(),
            padding=10
        )

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100, left=100),
            bgcolor=ft.colors.with_opacity(NAVBAR_SEARCH_OVERLAY_OPACITY, WHITE),
            padding=10,
            width=700,
            content=ft.Column(
                spacing=10,
                controls=[
                    self.title,
                    self.description,
                    self.tags,
                    ft.Stack(
                        controls=[
                            self.code_area,
                            ft.Container(
                                content=self.copy_code_button,
                                alignment=ft.alignment.top_right

                            )
                        ],
                    )
                ]
            )
        )

        return self.content
    
    def initialize(self):
        self.clear_controls()
        
        snippet_data = self.route.config.read_snippets_data(id=self.snippet_id)
        
        self.title.value = snippet_data.get('title', None)
        self.description.value = snippet_data.get('description', None)
        tags = [Tag(self, 60, 26, tag.get('color', None), tag.get('text', None)) for tag in snippet_data.get('tags', None)]
        self.tags.content.controls = tags
        tokens = snippet_data.get('tokens', None)
        
        if tokens is not None:
            self.fill_code_area(tokens)
       
        self.update()

    def fill_code_area(self, tokens):
        row_counter = 0
        indent = 0
        line_number = 1
        self.code_area.content.controls.append(ft.Row())
        self.code_area.content.controls[0].controls.append(ft.Text())
        self.code_area.content.controls[row_counter].controls[0].spans.append(ft.TextSpan(text=f"{line_number}    "))
        
        text_start = True  # Initialize text_start to True
        
        for token in tokens:
            #style = ft.TextStyle(color=COLORS.get(token[0], None))
            #spans = self.code_area.content.controls[row_counter].controls[0].spans

            if token[0] in ['NEWLINE', 'NL']:
                row_counter += 1
                line_number += 1
                self.code_area.content.controls.append(ft.Row())
                self.code_area.content.controls[row_counter].controls.append(ft.Text())
                self.code_area.content.controls[row_counter].controls[0].spans.append(ft.TextSpan(text=f"{line_number}    "))
                text_start = True  # Reset text_start on newline
                continue

            elif token[0] == 'INDENT':
                indent = len(token[1])
                continue
            
            elif token[0] == 'DEDENT':
                indent -= 4
                continue

            elif token[0] == 'SPACE':
                text = " "
            else:
                text = token[1]
            
            style = ft.TextStyle(color=COLORS.get(token[0], None))
            spans = self.code_area.content.controls[row_counter].controls[0].spans
            
            if text_start:
                text = f"{' ' * indent}{text}"
                text_start = False  # Set text_start to False after appending the first token
            
            spans.append(ft.TextSpan(text=text, style=style))

    def clear_controls(self):
        self.title.value = ""
        self.description.value = ""
        self.tags.content.controls.clear()
        self.code_area.content.controls.clear()
        self.update()

    def copy_code_to_clipboard(self, e):
        snippet_data = self.route.config.read_snippets_data(id=self.snippet_id)
        snippet_code = snippet_data.get('code', None)
        pyperclip.copy(snippet_code)
