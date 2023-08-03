import flet as ft

from components import TAG_PURPLE, TAG_PINK, TAG_BLUE, TAG_LIGHT_BLUE, TAG_LIGHT_BLUE_200, TAG_GREEN
from components import Tag, CodeCard, TagCard

class HomeView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        
        self.tag_card = TagCard(self.route, 300, 500, "Filter by tags")

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100, left=270),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=40,
                controls=[
                    ft.Column(),
                    ft.Column(
                        controls=[self.tag_card]
                    )
                ]
            )
        )

        return self.content

    def initialize(self):
        self.content.content.controls[0].controls.append(self.cards_grid())
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
    

        