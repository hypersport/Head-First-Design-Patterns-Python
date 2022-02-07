from pizza_store import PizzaStore
from chicago_style_clam_pizza import ChicagoStyleClamPizza
from chicago_style_cheese_pizza import ChicagoStyleCheesePizza
from chicago_style_pepperoni_pizza import ChicagoStylePepperoniPizza
from chicago_style_veggie_pizza import ChicagoStyleVeggiePizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, t: str):
        if t == 'cheese':
            return ChicagoStyleCheesePizza()
        elif t == 'pepperoni':
            return ChicagoStylePepperoniPizza()
        elif t == 'clam':
            return ChicagoStyleClamPizza()
        elif t == 'veggie':
            return ChicagoStyleVeggiePizza()
        else:
            return None
