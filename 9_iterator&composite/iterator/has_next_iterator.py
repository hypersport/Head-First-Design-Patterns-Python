from collections.abc import Iterator


class HasNextIterator(Iterator):
    def __init__(self, it):
        self.it = iter(it)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.it)

    def has_next(self):
        return self.it.__length_hint__() > 0
