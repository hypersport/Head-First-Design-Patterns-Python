from abstract_duck_factory import AbstractDuckFactory
from mallard_duck import MallardDuck
from duck_call import DuckCall
from rubber_duck import RubberDuck
from red_head_duck import RedHeadDuck


class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()

    def create_redhead_duck(self):
        return RedHeadDuck()
