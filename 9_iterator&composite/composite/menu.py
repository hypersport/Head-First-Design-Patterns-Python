from menu_component import MenuComponent
from has_next_iterator import HasNextIterator


class Menu(MenuComponent):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menu_components = []

    def add(self, menu_component):
        self.menu_components.append(menu_component)

    def remove(self, menu_component):
        self.menu_components.remove(menu_component)

    def get_child(self, i):
        return self.menu_components[i]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def print_(self):
        print(f'\n{self.get_name()}, {self.get_description()}---------------------')
        iterator = HasNextIterator(self.menu_components)
        while iterator.has_next():
            menu_component = next(iterator)
            menu_component.print_()
