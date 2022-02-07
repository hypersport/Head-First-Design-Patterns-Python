from pizza import Pizza


class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Style Clam Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')
        self.toppings.append('Frozen Clams from Chesapeake Bay')

    def cut(self):
        print('Cutting the pizza into square slices')
