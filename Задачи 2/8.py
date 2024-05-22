import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_on_x(self):
        return self.y == 0

    def is_on_y(self):
        return self.x == 0
