from menu import Menu
from menu_item import MenuItem
from has_next_iterator import HasNextIterator


class CafeMenu(Menu):
    def __init__(self):
        self.menu_items = {}
        self.add_item('Veggie Burger and Air Fries',
                      'Veggie burger on a whole wheat bun, lettuce, tomato, and fries',
                      True, 3.99)
        self.add_item('Soup of the day',
                      'A cup of the soup of the day, with a side salad',
                      False, 3.69)
        self.add_item('Burrito',
                      'A large burrito, with whole pinto beans, salsa, guacamole',
                      True, 4.29)

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items[menu_item.get_name()] = menu_item

    def get_items(self):
        return self.menu_items

    def create_iterator(self):
        return HasNextIterator(self.menu_items.values())
