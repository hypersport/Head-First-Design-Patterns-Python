from quackable import Quackable
from observable import Observable


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose
        self.observable = Observable(self)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    def quack(self):
        self.goose.honk()
        self.notify_observers()

    def __str__(self):
        return 'Goose pretending to be a Duck'
