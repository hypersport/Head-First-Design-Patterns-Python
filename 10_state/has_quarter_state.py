import random
from state import State


class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print('You can\'t insert another quarter.')

    def eject_quarter(self):
        print('Quarter returned.')
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def turn_crank(self):
        print('You turned...')
        winner = random.randrange(0, 10)
        if winner == 0 and self.gumball_machine.get_count() > 1:
            self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def dispense(self):
        print('No gumball dispensed.')

    def refill(self):
        pass

    def __str__(self):
        return 'waiting for turn of crank.'
