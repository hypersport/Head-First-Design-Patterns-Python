from quackable import Quackable


class Flock(Quackable):
    def __init__(self):
        self.ducks = []

    def register_observer(self, observer):
        for duck in self.ducks:
            duck.register_observer(observer)

    def notify_observers(self):
        pass

    def add(self, duck):
        self.ducks.append(duck)

    def quack(self):
        for duck in self.ducks:
            duck.quack()

    def __str__(self):
        return 'Flock of Ducks'
