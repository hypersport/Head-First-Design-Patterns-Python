class Pizza:
    name = ''
    dough = ''
    sauce = ''
    toppings = []

    def get_name(self):
        return self.name

    def prepare(self):
        print('Prepare ' + self.name)
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for topping in self.toppings:
            print('  ' + topping)

    def bake(self):
        print('Baking ' + self.name)

    def cut(self):
        print('Cutting ' + self.name)

    def box(self):
        print('Boxing ' + self.name)
