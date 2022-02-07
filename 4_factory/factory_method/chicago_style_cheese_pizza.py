from pizza import Pizza


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')
