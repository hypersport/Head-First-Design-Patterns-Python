from menu import Menu
from menu_item import MenuItem
from has_next_iterator import HasNextIterator


class PancakeHouseMenu(Menu):
    def __init__(self):
        self.menu_items = []
        self.add_item('K&B\'s Pancake Breakfast',
                      'Pancakes with scrambled eggs, and toast',
                      True, 2.99)
        self.add_item('Regular Pancake Breakfast',
                      'Pancakes with fried eggs, sausage',
                      False, 2.99)
        self.add_item('Blueberry Pancakes',
                      'Pancakes made with fresh blueberries, and blueberry syrup',
                      True, 3.49)
        self.add_item('Waffles',
                      'Waffles, with your choice of blueberries or strawberries',
                      True, 3.59)

    def add_item(self, name, description, vegetarian, price):
        menu_item = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    def get_items(self):
        return self.menu_items

    def create_iterator(self):
        return HasNextIterator(self.menu_items)
