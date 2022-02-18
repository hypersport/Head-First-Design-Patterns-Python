class Waitress:
    def __init__(self, menus):
        self.all_menus = menus

    def print_menu(self):
        self.all_menus.print_()
