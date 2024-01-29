import flet as ft
from constants import BODY_OPACITY, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT

from app import App


import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("flet_core").setLevel(logging.INFO)

if __name__ == '__main__':
    
    def main(page: ft.Page):
        page.title = "Code Snippet"
        page.window_resizable = False
        page.window_width = WINDOW_WIDTH
        page.window_height = WINDOW_HEIGHT
        page.padding = 0
        page.bgcolor = ft.colors.with_opacity(BODY_OPACITY, WHITE)
        page.scroll = "hidden"

        _app = App(page)
        page.on_route_change = _app.route_change

        page.add(_app.body)
        
        page.go('/home')
        page.update()

    ft.app(target=main)