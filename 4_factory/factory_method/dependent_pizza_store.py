from chicago_style_clam_pizza import ChicagoStyleClamPizza
from chicago_style_cheese_pizza import ChicagoStyleCheesePizza
from chicago_style_pepperoni_pizza import ChicagoStylePepperoniPizza
from chicago_style_veggie_pizza import ChicagoStyleVeggiePizza
from ny_style_clam_pizza import NYStyleClamPizza
from ny_style_cheese_pizza import NYStyleCheesePizza
from ny_style_pepperoni_pizza import NYStylePepperoniPizza
from ny_style_veggie_pizza import NYStyleVeggiePizza


class DependentPizzaStore:
    pizza = None

    def create_pizza(self, style: str, t: str):
        if style == 'NY':
            if t == 'cheese':
                self.pizza = NYStyleCheesePizza()
            elif t == 'pepperoni':
                self.pizza = NYStylePepperoniPizza()
            elif t == 'clam':
                self.pizza = NYStyleClamPizza()
            elif t == 'veggie':
                self.pizza = NYStyleVeggiePizza()
        elif style == 'Chicago':
            if t == 'cheese':
                self.pizza = ChicagoStyleCheesePizza()
            elif t == 'pepperoni':
                self.pizza = ChicagoStylePepperoniPizza()
            elif t == 'clam':
                self.pizza = ChicagoStyleClamPizza()
            elif t == 'veggie':
                self.pizza = ChicagoStyleVeggiePizza()
        else:
            print('Error: invalid type of pizza')
            return None

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza
