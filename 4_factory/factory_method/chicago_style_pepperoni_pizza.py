from pizza import Pizza


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Style Pepperoni Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')
        self.toppings.append('Black Olives')
        self.toppings.append('Spinach')
        self.toppings.append('Eggplant')
        self.toppings.append('Sliced Pepperoni')

    def cut(self):
        print('Cutting the pizza into square slices')
