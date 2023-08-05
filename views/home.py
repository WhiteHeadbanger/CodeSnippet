import flet as ft

from components import TAG_PURPLE
from components import Tag, CodeCard, TagCard

class HomeView(ft.UserControl):

    def __init__(self, route):
        super().__init__()
        self.route = route
        
        self.tag_card = TagCard(self.route, 300, 500, "Filter by tags")
        self.card_grid = ft.GridView(
            runs_count=3,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=40,
            run_spacing=40,
            width=1000
        )

    def build(self):
        self.content = ft.Container(
            margin=ft.margin.only(top=100, left=270),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=40,
                controls=[
                    ft.Column(
                        controls=[self.card_grid]
                    ),
                    ft.Column(
                        controls=[self.tag_card]
                    )
                ]
            )
        )

        return self.content

    def initialize(self):
        self.card_grid.controls.clear()
        self.cards_grid()
        self.update()
        
    def cards_grid(self):
        snippets_data = self.route.config.read_data()
        for snip in snippets_data:
            tags = [Tag(self.route, 60, 26, tag['color'], tag['text'], section="home") for tag in snip['tags']]

            self.card_grid.controls.append(CodeCard(snip['id'], self.route, 300, 300, snip['title'], snip['date'], snip['description'], tags, snip['code']))
    
    def add_new_snippet(self):


        pass