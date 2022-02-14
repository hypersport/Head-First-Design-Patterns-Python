from turkey import Turkey
import random


class DuckAdapter(Turkey):
    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        if random.randrange(0, 5) == 0:
            self.duck.fly()
