from quackable import Quackable

count = 0


class QuackCounter(Quackable):
    def __init__(self, duck):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        global count
        count += 1

    @staticmethod
    def get_quacks():
        return count
