import flet as ft
from components import BODY_OPACITY, WHITE, TAG_PURPLE
from components import NavBar, Tag, CodeCard

if __name__ == '__main__':
    
    def main(page: ft.Page):
        page.title = "Code Snippet"
        page.window_resizable = False
        page.window_width = 1920
        page.window_height = 1080
        page.padding = 0
        page.bgcolor = ft.colors.with_opacity(BODY_OPACITY, WHITE)
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # NavBar
        navbar = NavBar(width=1920, height=70)
        page.add(navbar)

        # Grid
        cards_grid = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=40,
            run_spacing=40,
            width=1000
        )

        # Tags
        python_tag = Tag(60, 26, TAG_PURPLE, "Python")

        for i in range(6):
            cards_grid.controls.append(CodeCard(300, 300, "Hello World", "now", "A snippet to create a hello world", python_tag))
        
        """ cards_grid_col = ft.Column(
            controls=[cards_grid]
        )

        filters_col = ft.Column(
            controls=[CodeCard(300, 300, "Hello World", "now", "A snippet to create a hello world", python_tag)]
        )

        main_row = ft.Row(
            controls=[
                cards_grid_col,
                filters_col
            ]
        )

        page.add(main_row) """
        page.add(cards_grid)
        
        page.update()

    ft.app(target=main)