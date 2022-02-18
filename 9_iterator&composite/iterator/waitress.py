class Waitress:
    def __init__(self, pancake_house_menu, diner_menu, cafe_menu):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu
        self.cafe_menu = cafe_menu

    def print_menu(self, iterator=None):
        if iterator:
            while iterator.has_next():
                menu_item = next(iterator)
                print(f'{menu_item.get_name()}, '
                      f'{menu_item.get_price()} -- '
                      f'{menu_item.get_description()}')
        else:
            pancake_iterator = self.pancake_house_menu.create_iterator()
            diner_iterator = self.diner_menu.create_iterator()
            cafe_iterator = self.cafe_menu.create_iterator()
            print('MENU\n----\nBREAKFAST')
            self.print_menu(pancake_iterator)
            print('\nLUNCH')
            self.print_menu(diner_iterator)
            print('\nDINNER')
            self.print_menu(cafe_iterator)

    def print_vegetarian_menu(self, iterator=None):
        if iterator:
            while iterator.has_next():
                menu_item = next(iterator)
                if menu_item.is_vegetarian():
                    print(f'{menu_item.get_name()}, '
                          f'{menu_item.get_price()} -- '
                          f'{menu_item.get_description()}')
            else:
                print('\nVEGETARIAN MENU\n---------------')
                self.print_vegetarian_menu(self.pancake_house_menu.create_iterator())
                self.print_vegetarian_menu(self.diner_menu.create_iterator())
                self.print_vegetarian_menu(self.cafe_menu.create_iterator())

    def is_item_vegetarian(self, name):
        pancake_iterator = self.pancake_house_menu.create_iterator()
        if self.is_vegetarian(name, pancake_iterator):
            return True

        diner_iterator = self.diner_menu.create_iterator()
        if self.is_vegetarian(name, diner_iterator):
            return True

        cafe_iterator = self.cafe_menu.create_iterator()
        if self.is_vegetarian(name, cafe_iterator):
            return True

        return False

    @staticmethod
    def is_vegetarian(name, iterator):
        while iterator.has_next():
            menu_item = next(iterator)
            return True if menu_item.get_name == name and menu_item.is_vegetarian() else False
