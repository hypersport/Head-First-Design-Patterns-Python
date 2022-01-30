from duck import Duck
from fly_no_way import FlyNoWay
from quack import Quack


class ModelDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyNoWay())
        self.set_quack_behavior(Quack())

    def display(self):
        print('I\'m a real Model Duck')
