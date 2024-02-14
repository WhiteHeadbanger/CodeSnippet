import flet as ft
from components import NavBar
from views import HomeView, NewSnippetView, SnippetView, EditSnippetView, AuthView
from config import Config
from auth import Session

class App:

    def __init__(self, page: ft.Page):
        self.page = page

        self.session = Session()

        # Creates the navbar
        self.navbar = NavBar(self, self.session)

        # Instances of views. Passing self as a parameter to facilitate communication between all views
        self.home = HomeView(self)
        self.new_snippet = NewSnippetView(self)
        self.snippet = SnippetView(self)
        self.edit_snippet = EditSnippetView(self)
        self.auth = AuthView(self)
        
        # Instance of Config
        self.config = Config(self)

        # Creates dict of routes
        self.routes = {
            '/home': self.home,
            '/newsnippet': self.new_snippet,
            '/snippet': self.snippet,
            '/editsnippet': self.edit_snippet,
            '/auth': self.auth,
        }

        # Creates dict of methods to initialize the views
        self.calls = {
            '/home': self.home.initialize,
            '/newsnippet': self.new_snippet.initialize,
            '/snippet': self.snippet.initialize,
            '/editsnippet': self.edit_snippet.initialize,
            '/auth': self.auth.initialize,
        }

        # App body
        self.container = ft.Container(content=self.routes['/home'], alignment=ft.alignment.center)
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