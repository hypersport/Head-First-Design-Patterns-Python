import abc
from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior


class Duck(metaclass=abc.ABCMeta):
    fly_behavior = None
    quack_behavior = None

    def set_fly_behavior(self, fly_behavior):
        if isinstance(fly_behavior, FlyBehavior):
            self.fly_behavior = fly_behavior
        else:
            raise Exception('Param is not an instance of FlyBehavior')

    def set_quack_behavior(self, quack_behavior):
        if isinstance(quack_behavior, QuackBehavior):
            self.quack_behavior = quack_behavior
        else:
            raise Exception('Param is not an instance of QuackBehavior')

    def perform_fly(self):
        if self.fly_behavior:
            self.fly_behavior.fly()
        else:
            print('This duck can\'t fly.')

    def perform_quack(self):
        if self.quack_behavior:
            self.quack_behavior.quack()
        else:
            print('This duck can\'t quack.')

    @staticmethod
    def swim():
        print('All strategy float, even decoys!')

    @abc.abstractmethod
    def display(self):
        raise Exception('Abstract methods must be implemented')
