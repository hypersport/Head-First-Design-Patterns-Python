from pizza_store import PizzaStore
from ny_style_clam_pizza import NYStyleClamPizza
from ny_style_cheese_pizza import NYStyleCheesePizza
from ny_style_pepperoni_pizza import NYStylePepperoniPizza
from ny_style_veggie_pizza import NYStyleVeggiePizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, t: str):
        if t == 'cheese':
            return NYStyleCheesePizza()
        elif t == 'pepperoni':
            return NYStylePepperoniPizza()
        elif t == 'clam':
            return NYStyleClamPizza()
        elif t == 'veggie':
            return NYStyleVeggiePizza()
        else:
            return None
