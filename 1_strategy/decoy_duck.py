from duck import Duck
from fly_no_way import FlyNoWay
from mute_quack import MuteQuack


class ModelDuck(Duck):
    def __init__(self):
        self.set_fly_behavior(FlyNoWay())
        self.set_quack_behavior(MuteQuack())

    def display(self):
        print('I\'m a real Duck Decoy')
