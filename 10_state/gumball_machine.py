from has_quarter_state import HasQuarterState
from no_quarter_state import NoQuarterState
from sold_out_state import SoldOutState
from sold_state import SoldState
from winner_state import WinnerState


class GumballMachine:
    def __init__(self, number_gumballs):
        self.has_quarter_state = HasQuarterState(self)
        self.no_quarter_state = NoQuarterState(self)
        self.sold_out_state = SoldOutState(self)
        self.sold_state = SoldState(self)
        self.winner_state = WinnerState(self)

        self.state = self.sold_out_state
        self.count = number_gumballs
        if number_gumballs > 0:
            self.state = self.no_quarter_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print('A gumball comes rolling out the slot...')
        if self.count != 0:
            self.count -= 1

    def get_count(self):
        return self.count

    def refill(self, count):
        self.count += count
        print(f'The gumball machine was just refilled; it\'s new count is: {self.count}.')
        self.state.refill()

    def get_state(self):
        return self.state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_winner_state(self):
        return self.winner_state

    def __str__(self):
        result = ['\nMighty Gumball, Inc.', f'\nInventory: {self.count} gumball']
        if self.count != 1:
            result.append('s')
        result.append(f'\nMachine is {self.state}\n')
        return ''.join(result)
