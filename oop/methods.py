# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: doesn't depend on the class or any instance
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    # Class method: has access to class attributes through 'cls'
    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and show calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
