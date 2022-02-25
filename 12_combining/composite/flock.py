from quackable import Quackable


class Flock(Quackable):
    def __init__(self):
        self.quackers = []

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()
