from menu_component import MenuComponent


class MenuItem(MenuComponent):
    def __init__(self, name, desc, vegetarian, price):
        self.name = name
        self.description = desc
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def print_(self):
        print(f' {self.get_name()}', end='')
        if self.is_vegetarian():
            print('(v)', end='')
        print(f', {self.get_price()}     -- {self.get_description()}')
