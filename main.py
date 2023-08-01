import flet as ft
from components import BODY_OPACITY, WHITE, TAG_PURPLE, TAG_PINK, TAG_BLUE, TAG_LIGHT_BLUE, TAG_LIGHT_BLUE_200, TAG_GREEN
from components import NavBar, Tag, CodeCard, TagCard

if __name__ == '__main__':
    
    def main(page: ft.Page):
        page.title = "Code Snippet"
        page.window_resizable = False
        page.window_width = 1920
        page.window_height = 1080
        page.padding = 0
        page.bgcolor = ft.colors.with_opacity(BODY_OPACITY, WHITE)
        #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # NavBar
        navbar = NavBar(width=1920, height=70)
        page.add(navbar)

        # Grid
        cards_grid = ft.GridView(
            runs_count=3,
            max_extent=300,
            child_aspect_ratio=1.0,
            spacing=40,
            run_spacing=40,
            width=1000
        )

        # Tags
        python_tag = Tag(60, 26, TAG_PURPLE, "Python")
        javascript_tag = Tag(60, 26, TAG_BLUE, "JavaScript")
        c_tag = Tag(60, 26, TAG_LIGHT_BLUE, "C")
        cplusplus_tag = Tag(60, 26, TAG_LIGHT_BLUE_200, "C++")
        go_tag = Tag(60, 26, TAG_PINK, "Go")
        react_tag = Tag(60, 26, TAG_GREEN, "React")

        for i in range(12):
            cards_grid.controls.append(CodeCard(300, 300, "Hello World", "now", "A snippet to create a hello world", python_tag))
        
        # Main body
        cards_grid_col = ft.Column(
            controls=[cards_grid]
        )

        filters_tags = [
            python_tag,
            javascript_tag,
            c_tag,
            cplusplus_tag,
            go_tag,
            react_tag
        ]
        filters_col = ft.Column(
            controls=[TagCard(300, 500, "Filter by tags", python_tag, javascript_tag, c_tag, cplusplus_tag, go_tag, react_tag)]
        )

        main_row = ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=40,
            controls=[
                cards_grid_col,
                filters_col
            ]
        )

        main_container = ft.Container(
            #bgcolor=ft.colors.RED_900,
            margin=ft.margin.only(top=100, left=270),
            content=main_row
                        
        )
        

        page.add(main_container)
        
        page.update()

    ft.app(target=main)