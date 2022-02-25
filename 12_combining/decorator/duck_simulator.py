from mallard_duck import MallardDuck
from rubber_duck import RubberDuck
from duck_call import DuckCall
from red_head_duck import RedHeadDuck
from goose_adapter import GooseAdapter
from goose import Goose
from quack_counter import QuackCounter


class DuckSimulator:
    @staticmethod
    def simulate():
        mallard_duck = QuackCounter(MallardDuck())
        rubber_duck = QuackCounter(RubberDuck())
        duck_call = QuackCounter(DuckCall())
        red_head_duck = QuackCounter(RedHeadDuck())
        goose_duck = GooseAdapter(Goose())

        def inner_simulate(duck):
            duck.quack()

        inner_simulate(mallard_duck)
        inner_simulate(rubber_duck)
        inner_simulate(duck_call)
        inner_simulate(red_head_duck)
        inner_simulate(goose_duck)
        print(QuackCounter.get_quacks())


if __name__ == '__main__':
    DuckSimulator().simulate()
