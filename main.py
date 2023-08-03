import flet as ft
from components import BODY_OPACITY, WHITE
from views.home import _home_view_
from views.new_tag import _newtag_view_

#TODO '/newtag', '/snippet', '/newsnippet'

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("flet_core").setLevel(logging.INFO)

if __name__ == '__main__':
    
    def main(page: ft.Page):
        page.title = "Code Snippet"
        page.window_resizable = False
        page.window_width = 1920
        page.window_height = 1080
        page.padding = 0
        page.bgcolor = ft.colors.with_opacity(BODY_OPACITY, WHITE)
        page.scroll = "auto"

        home = _home_view_(page)
        new_tag = _newtag_view_(page)

        def route_change(route):
            page.views.clear()
            if page.route == '/newtag':
                page.views.append(new_tag)
            elif page.route == '/home':
                page.views.append(home)

            page.update()

        def view_pop(view):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)

        page.views.append(home)
        
        page.update()

    ft.app(target=main)