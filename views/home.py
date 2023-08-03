import flet as ft

from . import BaseView
from components import TAG_PURPLE, TAG_PINK, TAG_BLUE, TAG_LIGHT_BLUE, TAG_LIGHT_BLUE_200, TAG_GREEN
from components import Tag, CodeCard, TagCard

class HomeView(BaseView):

    def __init__(self, page, *args, **kwargs):
        super().__init__(page, *args, **kwargs)
        self.route = '/home'
        self.scroll = 'auto'
        self.test_text = ft.Text(value="hola")
        self.controls = [
            self.navbar,
            ft.Container(
                margin=ft.margin.only(top=100, left=270),
                content=ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=40,
                    controls=[
                        ft.Column(
                            controls=[self.cards_grid()]
                        ),
                        ft.Column(
                            controls=[TagCard(300, 500, "Filter by tags"), self.test_text]
                        )
                    ]
                )
            )
        ]

    def update(self):
        super().update()
        if self.page.client_storage.contains_key('tag'):
            new_tag = self.page.client_storage.get('tag')
            self.test_text.value = new_tag
            name, color = new_tag[0], new_tag[1]
            if color == 'purple':
                color = TAG_PURPLE
            elif color == 'pink':
                color = TAG_PINK
            elif color == 'blue':
                color = TAG_BLUE
            elif color == 'green':
                color = TAG_GREEN
            self.controls[1].content.controls[1].controls[0].add_tag(Tag(60, 26, color, name))
        self.test_text.value = "Home Actualizado"


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
            cards_grid.controls.append(CodeCard(300, 300, "Hello World", "now", "A snippet to create a hello world", [python_tag]))

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

def _home_view_(page):
    return HomeView(page)

        