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

        self.content = ft.Container(
            margin=ft.margin.only(top=100),
            content=ft.ResponsiveRow(
                spacing=40,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Column(
                        col=6,
                        controls=[self.card_grid]
                    ),
                    ft.Column(
                        col=2,
                        controls=[self.tag_card]
                    )
                ]
            )
        )

        self.delete_snippet_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirm delete"),
            content=ft.Text(f"Are you sure you want to delete this snippet?"),
            actions=[
                ft.TextButton("Yes", on_click=self.delete_snippet),
                ft.TextButton("No", on_click=self.close_dialog)
            ]
        )

        self.stack = ft.Stack(
            controls=[
                self.content,
                self.delete_snippet_dialog
            ]
        )

    def build(self):
        return self.stack

    def initialize(self):
        self.card_grid.controls.clear()
        self.tag_card.clear_tags()
        self.cards_grid()
        self.load_tags()
        self.update()
        
    def cards_grid(self):
        #TODO use pydantic to create a snippet object from json
        snippets_data = self.route.config.read_snippets_data()
        for snip in snippets_data:
            tags = [Tag(self, 60, 26, tag['color'], tag['text']) for tag in snip['tags']]

            self.card_grid.controls.append(CodeCard(snip['id'], self.route, 300, 300, snip['title'], snip['date'], snip['description'], tags, snip['code']))
    
    def load_tags(self):
        tags_data = self.route.config.read_tags_data()
        for tag in tags_data:
            self.tag_card.add_tag(Tag(self, 60, 26, tag.color, tag.text))

    
    def delete_snippet(self, e):
        # Get card instance from dialog data
        card = self.delete_snippet_dialog.data
        self.delete_snippet_dialog.open = False

        # Get data from json
        snippets_data = self.route.config.read_snippets_data()
        
        # Extract the snipet from database by ID
        snippet_to_remove = None
        for snip in snippets_data:
            if snip['id'] == card.id:
                snippet_to_remove = snip
        
        # Remove snippet from database
        snippets_data.remove(snippet_to_remove)

        # Save database
        self.route.config.save_snippets_data(snippets_data)
        
        # Remove card from card grid
        self.card_grid.controls.remove(card)
        self.update()

    
    def open_dialog(self, card):
        self.route.page.dialog = self.delete_snippet_dialog
        self.delete_snippet_dialog.open = True
        self.delete_snippet_dialog.data = card
        self.update()

    def close_dialog(self, e):
        self.delete_snippet_dialog.open = False
        self.update()