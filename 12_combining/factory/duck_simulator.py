from counting_duck_factory import CountingDuckFactory
from goose_adapter import GooseAdapter
from goose import Goose
from quack_counter import QuackCounter


class DuckSimulator:
    @staticmethod
    def simulate():
        duck_factory = CountingDuckFactory()
        mallard_duck = duck_factory.create_mallard_duck()
        rubber_duck = duck_factory.create_rubber_duck()
        duck_call = duck_factory.create_duck_call()
        red_head_duck = duck_factory.create_redhead_duck()
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
