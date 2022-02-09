class ChocolateBoiler:
    unique_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.unique_instance:
            cls.unique_instance = super().__new__(cls, *args, **kwargs)
        return cls.unique_instance

    def __init__(self):
        self.empty = True
        self.boiled = False

    def is_empty(self):
        return self.empty

    def is_boiled(self):
        return self.boiled

    def fill(self):
        if self.is_empty():
            self.empty = False
            self.boiled = False

    def drain(self):
        if not self.is_empty() and self.is_boiled():
            self.empty = True

    def boil(self):
        if not self.is_empty() and not self.is_boiled():
            self.boiled = True
