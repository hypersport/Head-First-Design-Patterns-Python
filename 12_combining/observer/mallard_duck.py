from quackable import Quackable
from observable import Observable


class MallardDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        print('Quack')
        self.notify_observers()

    def __str__(self):
        return 'Mallard Duck'
