from flet import View
from components import NavBar

class BaseView(View):

    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.navbar = NavBar(1920, 70)
        self.page = page
        

