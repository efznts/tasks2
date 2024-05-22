class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition:
            print('Газировка и', self.addition)
        else:
            print('Обычная газировка')
