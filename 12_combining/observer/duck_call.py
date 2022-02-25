from observable import Observable
from quackable import Quackable


class DuckCall(Quackable):
    def __init__(self):
        self.observable = Observable(self)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        print('Kwak')
        self.notify_observers()

    def __str__(self):
        return 'Duck Call'
