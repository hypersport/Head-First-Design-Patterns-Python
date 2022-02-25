from quackable import Quackable

count = 0


class QuackCounter(Quackable):
    def __init__(self, duck):
        self.duck = duck

    def register_observer(self, observer):
        self.duck.register_observer(observer)

    def notify_observers(self):
        self.duck.notify_observers()

    def quack(self):
        self.duck.quack()
        global count
        count += 1

    @staticmethod
    def get_quacks():
        return count

    def __str__(self):
        return str(self.duck)
