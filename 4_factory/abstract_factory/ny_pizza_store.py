from pizza_store import PizzaStore
from ny_pizza_ingredient_factory import NYPizzaIngredientFactory
from cheese_pizza import CheesePizza
from clam_pizza import ClamPizza
from pepperoni_pizza import PepperoniPizza
from veggie_pizza import VeggiePizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, t: str):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if t == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('New York Style Cheese Pizza')
        elif t == 'pepperoni':
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name('New York Style Pepperoni Pizza')
        elif t == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('New York Style Clam Pizza')
        elif t == 'veggie':
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name('New York Style Veggie Pizza')
        return pizza
