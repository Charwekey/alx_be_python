# main.py
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # List of shape objects
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrating polymorphism
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
