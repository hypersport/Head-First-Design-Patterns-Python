class Screen:
    def __init__(self, desc):
        self.description = desc

    def up(self):
        print(f'{self.description} going up.')

    def down(self):
        print(f'{self.description} going down.')

    def __str__(self):
        return self.description
