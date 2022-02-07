from pizza_ingredient_factory import PizzaIngredientFactory
from thin_crust_dough import ThinCrustDough
from reggiano_cheese import ReggianoCheese
from marinara_sauce import MarinaraSauce
from sliced_pepperoni import SlicedPepperoni
from fresh_clams import FreshClams
from garlic import Garlic
from onion import Onion
from red_pepper import RedPepper
from mushroom import Mushroom


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()
