import flet as ft
from components import NavBar
from views import HomeView, NewTagView, NewSnippetView, SnippetView, EditSnippetView
from config import Config

class App:

    def __init__(self, page: ft.Page):
        self.page = page

        # Creates the navbar
        self.navbar = NavBar(self, width=1920, height=70)

        # Instances of views. Passing self as a parameter to facilitate communication between all views
        self.home = HomeView(self)
        self.new_tag = NewTagView(self)
        self.new_snippet = NewSnippetView(self)
        self.snippet = SnippetView(self)
        self.edit_snippet = EditSnippetView(self)
        
        self.config = Config(self)

        # Creates dict of routes
        self.routes = {
            '/home': self.home,
            '/newtag': self.new_tag,
            '/newsnippet': self.new_snippet,
            '/snippet': self.snippet,
            '/editsnippet': self.edit_snippet
        }

        # Creates dict of methods to initialize the views
        self.calls = {
            '/home': self.home.initialize,
            '/newtag': self.new_tag.initialize,
            '/newsnippet': self.new_snippet.initialize,
            '/snippet': self.snippet.initialize,
            '/editsnippet': self.edit_snippet.initialize
        }

        # App body
        self.container = ft.Container(content=self.routes['/home'])
        self.body = ft.Column(
            expand=True,
            controls=[
                self.navbar,
                self.container
            ]
        )

    def route_change(self, e):
        # Change View
        self.container.content = self.routes[e.route]
        self.page.update()

        # Initialize the view
        self.calls[e.route]()

        self.page.update()