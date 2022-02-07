from pizza_store import PizzaStore
from chicago_pizza_ingredient_factory import ChicagoPizzaIngredientFactory
from cheese_pizza import CheesePizza
from clam_pizza import ClamPizza
from pepperoni_pizza import PepperoniPizza
from veggie_pizza import VeggiePizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, t: str):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if t == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('Chicago Style Cheese Pizza')
        elif t == 'pepperoni':
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name('Chicago Style Pepperoni Pizza')
        elif t == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('Chicago Style Clam Pizza')
        elif t == 'veggie':
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name('Chicago Style Veggie Pizza')
        return pizza
