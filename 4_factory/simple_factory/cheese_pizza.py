from pizza import Pizza


class CheesePizza(Pizza):
    def __init__(self):
        self.name = 'Cheese Pizza'
        self.dough = 'Regular Crust'
        self.sauce = 'Marinara Pizza Sauce'
        self.toppings.append('Fresh Mozzarella')
        self.toppings.append('Parmesan')
