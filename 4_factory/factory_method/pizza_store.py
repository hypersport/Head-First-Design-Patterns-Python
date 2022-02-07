import abc


class PizzaStore(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_pizza(self, t: str):
        raise Exception('Abstract methods must be implemented')

    def order_pizza(self, t: str):
        pizza = self.create_pizza(t)
        print('--- Making a ' + pizza.get_name() + ' ---')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
