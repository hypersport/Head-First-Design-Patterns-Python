from pizza import Pizza


class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = 'Pepperoni Pizza'
        self.dough = 'Crust'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('Sliced Pepperoni')
        self.toppings.append('Sliced Onion')
        self.toppings.append('Grated parmesan cheese')
