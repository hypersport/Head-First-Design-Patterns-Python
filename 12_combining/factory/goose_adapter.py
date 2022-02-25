from quackable import Quackable


class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose

    def quack(self):
        self.goose.honk()

    def __str__(self):
        return 'Goose pretending to be a Duck'
