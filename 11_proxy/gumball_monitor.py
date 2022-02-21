class GumballMonitor:
    def __init__(self, machine):
        self.machine = machine

    def report(self):
        try:
            print(f'Gumball Machine: {self.machine.get_location()}')
            print(f'Current inventory: {self.machine.get_count()} gumballs')
        except Exception as e:
            print(e)
