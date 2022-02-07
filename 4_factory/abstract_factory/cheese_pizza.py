from pizza import Pizza
from pizza_ingredient_factory import PizzaIngredientFactory


class CheesePizza(Pizza):
    ingredient_factory = None

    def __init__(self, factory):
        if isinstance(factory, PizzaIngredientFactory):
            self.ingredient_factory = factory

    def prepare(self):
        print('Preparing ' + self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
