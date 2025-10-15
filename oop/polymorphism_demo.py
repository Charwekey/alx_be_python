# polymorphism_demo.py
import math

# Base class
class Shape:
    def area(self):
        # This method is meant to be overridden by subclasses
        raise NotImplementedError("Subclasses must override this method")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Overriding the area method
    def area(self):
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the area method
    def area(self):
        return math.pi * (self.radius ** 2)
