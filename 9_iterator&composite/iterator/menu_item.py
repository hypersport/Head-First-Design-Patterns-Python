class MenuItem:
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
