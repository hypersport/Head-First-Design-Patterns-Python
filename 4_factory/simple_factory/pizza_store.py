from simple_pizza_factory import SimplePizzaFactory


class PizzaStore:
    factory = None

    def __init__(self, factory):
        if isinstance(factory, SimplePizzaFactory):
            self.factory = factory

    def order_pizza(self, t: str):
        pizza = self.factory.create_pizza(t)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
