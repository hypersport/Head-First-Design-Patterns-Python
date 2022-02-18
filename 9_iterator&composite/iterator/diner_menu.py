from menu import Menu
from menu_item import MenuItem
from has_next_iterator import HasNextIterator
from typing import Final


class DinerMenu(Menu):
    MAX_ITEMS: Final = 6

    def __init__(self):
        self.number_of_items = 0
        self.menu_items = []
        self.add_item('Vegetarian BLT',
                      '(Fakin\') Bacon with lettuce & tomato on whole wheat',
                      True, 2.99)
        self.add_item('BLT',
                      'Bacon with lettuce & tomato on whole wheat',
                      False, 2.99)
        self.add_item('Soup of the day',
                      'Soup of the day, with a side of potato salad',
                      False, 3.29)
        self.add_item('Hotdog',
                      'A hot dog, with saurkraut, relish, onions, topped with cheese',
                      False, 3.05)
        self.add_item('Steamed Veggies and Brown Rice',
                      'A medly of steamed vegetables over brown rice',
                      True, 3.99)
        self.add_item('Pasta',
                      'Spaghetti with Marinara Sauce, and a slice of sourdough bread',
                      True, 3.89)

    def add_item(self, name, description, vegetarian, price):
        if self.number_of_items > self.MAX_ITEMS:
            print('Sorry, menu is full!  Cannot add item to menu.')
        else:
            menu_item = MenuItem(name, description, vegetarian, price)
            self.menu_items.append(menu_item)
            self.number_of_items += 1

    def get_items(self):
        return self.menu_items

    def create_iterator(self):
        return HasNextIterator(self.menu_items)
