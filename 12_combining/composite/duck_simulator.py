from counting_duck_factory import CountingDuckFactory
from goose_adapter import GooseAdapter
from goose import Goose
from quack_counter import QuackCounter
from flock import Flock


class DuckSimulator:
    @staticmethod
    def simulate():
        def inner_simulate(duck):
            duck.quack()

        duck_factory = CountingDuckFactory()

        rubber_duck = duck_factory.create_rubber_duck()
        duck_call = duck_factory.create_duck_call()
        red_head_duck = duck_factory.create_redhead_duck()
        goose_duck = GooseAdapter(Goose())
        flock_ducks = Flock()
        flock_ducks.add(rubber_duck)
        flock_ducks.add(duck_call)
        flock_ducks.add(red_head_duck)
        flock_ducks.add(goose_duck)

        mallard_duck1 = duck_factory.create_mallard_duck()
        mallard_duck2 = duck_factory.create_mallard_duck()
        mallard_duck3 = duck_factory.create_mallard_duck()
        mallard_duck4 = duck_factory.create_mallard_duck()
        flock_mallards = Flock()
        flock_mallards.add(mallard_duck1)
        flock_mallards.add(mallard_duck2)
        flock_mallards.add(mallard_duck3)
        flock_mallards.add(mallard_duck4)

        flock_ducks.add(flock_mallards)

        print('\nDuck Simulator: Whole Flock Simulation:')
        inner_simulate(flock_ducks)
        print('\nDuck Simulator: Mallard Flock Simulation:')
        inner_simulate(flock_mallards)

        print(QuackCounter.get_quacks())


if __name__ == '__main__':
    DuckSimulator().simulate()
