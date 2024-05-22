class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def increase_quantity(self, amount):
        if amount > 0:
            self.quantity += amount

    def decrease_quantity(self, amount):
        self.quantity -= amount

    def total_cost(self):
        return self.price * self.quantity
