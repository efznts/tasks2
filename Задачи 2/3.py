class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_triangle(self):
        a, b, c = self.sides

        if not all(isinstance(side, (int, float)) for side in self.sides):
            return 'Нужно вводить только числа!'

        if any(side <= 0 for side in self.sides):
            return 'С отрицательными числами ничего не выйдет!'

        if a + b > c and a + c > b and b + c > a:
            return 'Ура, можно построить треугольник!'
        else:
            return 'Жаль, но из этого треугольник не сделать.'
