from observer import Observer


class Quackologist(Observer):
    def update(self, duck):
        print(f'Quackologist {str(duck)} just quacked.')

    def __str__(self):
        return 'Quackologist'
