from pizza import Pizza


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Deep Dish Veggie Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')
        self.toppings.append('Black Olives')
        self.toppings.append('Spinach')
        self.toppings.append('Eggplant')

    def cut(self):
        print('Cutting the pizza into square slices')
