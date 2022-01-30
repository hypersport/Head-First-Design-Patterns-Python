from duck import Duck
from fly_no_way import FlyNoWay
from squeak import Squeak


class RubberDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyNoWay())
        self.set_quack_behavior(Squeak())

    def display(self):
        print('I\'m a real Rubber Duck')
