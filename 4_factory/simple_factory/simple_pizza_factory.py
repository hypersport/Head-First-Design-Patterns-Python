from cheese_pizza import CheesePizza
from pepperoni_pizza import PepperoniPizza
from clam_pizza import ClamPizza
from veggie_pizza import VeggiePizza


class SimplePizzaFactory:
    pizza = None

    def create_pizza(self, t: str):
        if t == 'cheese':
            self.pizza = CheesePizza()
        elif t == 'pepperoni':
            self.pizza = PepperoniPizza()
        elif t == 'clam':
            self.pizza = ClamPizza()
        elif t == 'veggie':
            self.pizza = VeggiePizza()
        return self.pizza
