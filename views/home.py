import flet as ft

from components import TAG_PURPLE, TAG_PINK, TAG_BLUE, TAG_LIGHT_BLUE, TAG_LIGHT_BLUE_200, TAG_GREEN
from components import Tag, CodeCard, TagCard

class HomeView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100, left=270),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=40,
                controls=[
                    ft.Column(
                        controls=[]
                    ),
                    ft.Column(
                        controls=[]
                    )
                ]
            )
        )

        return self.content

    def initialize(self):
        self.content.content.controls[0].controls.append(self.cards_grid())
        self.content.content.controls[1].controls.append(TagCard(self.route, 300, 500, "Filter by tags"))
        self.update()

    def cards_grid(self):
        cards_grid = ft.GridView(
            runs_count=3,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=40,
            run_spacing=40,
            width=1000
        )

        python_tag = Tag(60, 26, TAG_PURPLE, "Python")

        for i in range(12):
            cards_grid.controls.append(CodeCard(self.route, 300, 300, "Hello World", "now", "A snippet to create a hello world", [python_tag]))

        return cards_grid
    
    def get_tags(self):
        # Tags
        python_tag = Tag(60, 26, TAG_PURPLE, "Python")
        javascript_tag = Tag(60, 26, TAG_BLUE, "JS")
        c_tag = Tag(60, 26, TAG_LIGHT_BLUE, "C")
        cplusplus_tag = Tag(60, 26, TAG_LIGHT_BLUE_200, "C++")
        go_tag = Tag(60, 26, TAG_PINK, "Go")
        react_tag = Tag(60, 26, TAG_GREEN, "React")

        return [python_tag, javascript_tag, c_tag, cplusplus_tag, go_tag, react_tag]

        