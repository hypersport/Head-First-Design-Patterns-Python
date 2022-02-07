from pizza_ingredient_factory import PizzaIngredientFactory
from thick_crust_dough import ThickCrustDough
from plum_tomato_sauce import PlumTomatoSauce
from mozzarella_cheese import MozzarellaCheese
from sliced_pepperoni import SlicedPepperoni
from frozen_clams import FrozenClams
from eggplant import Eggplant
from black_olives import BlackOlives
from spinach import Spinach


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [BlackOlives(), Spinach(), Eggplant()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()
