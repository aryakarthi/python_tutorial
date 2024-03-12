from abc import ABC, abstractmethod
import math


class Shape(ABC):

    # Abstract method
    @abstractmethod
    def area(self):
        pass

    # Abstract method
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing the abstract method area
    def area(self):
        return self.width * self.height

    # Implementing the abstract method perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Creating an instance of Rectangle
rectangle = Rectangle(3, 4)
print(f"Rectangle area: {rectangle.area()}")  # Output: 12
print(f"Rectangle perimeter: {rectangle.perimeter()}")  # Output: 14


# Creating an instance of Circle
circle = Circle(5)
print(f"Circle area: {circle.area():.2f}")  # Output: 78.54
print(f"Circle perimeter: {circle.perimeter():.2f}")  # Output: 31.42
