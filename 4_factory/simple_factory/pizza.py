class Pizza:
    name = ''
    dough = ''
    sauce = ''
    toppings = []

    def get_name(self):
        return self.name

    def prepare(self):
        print('Preparing ' + self.name)

    def bake(self):
        print('Baking ' + self.name)

    def cut(self):
        print('Cutting ' + self.name)

    def box(self):
        print('Boxing ' + self.name)
