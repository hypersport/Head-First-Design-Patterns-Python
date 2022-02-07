from pizza import Pizza


class ClamPizza(Pizza):
    def __init__(self):
        self.name = 'Clam Pizza'
        self.dough = 'Thin crust'
        self.sauce = 'White garlic sauce'
        self.toppings.append('Clams')
        self.toppings.append('Grated parmesan cheese')
