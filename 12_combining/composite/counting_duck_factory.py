from abstract_duck_factory import AbstractDuckFactory
from mallard_duck import MallardDuck
from duck_call import DuckCall
from rubber_duck import RubberDuck
from red_head_duck import RedHeadDuck
from quack_counter import QuackCounter


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedHeadDuck())
