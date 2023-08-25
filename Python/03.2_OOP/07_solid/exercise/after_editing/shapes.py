from abc import ABC, abstractmethod
from math import pi


class Figure:

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height * 0.5


class Square(Figure):

    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width * self.width


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)


class AreaCalculator:

    def __init__(self, shapes: list):
        if not isinstance(shapes, list):
            raise AssertionError("`shapes` should be of type `list`.")

        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)


# бонус тест:

# shapes = [Rectangle(2, 5), Triangle(2, 3), Square(3), Circle(5)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)