from mallard_duck import MallardDuck
from rubber_duck import RubberDuck
from duck_call import DuckCall
from red_head_duck import RedHeadDuck


class DuckSimulator:
    @staticmethod
    def simulate():
        mallard_duck = MallardDuck()
        rubber_duck = RubberDuck()
        duck_call = DuckCall()
        red_head_duck = RedHeadDuck()

        def inner_simulate(duck):
            duck.quack()

        inner_simulate(mallard_duck)
        inner_simulate(rubber_duck)
        inner_simulate(duck_call)
        inner_simulate(red_head_duck)


if __name__ == '__main__':
    DuckSimulator().simulate()
