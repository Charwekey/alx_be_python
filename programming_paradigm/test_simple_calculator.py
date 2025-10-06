import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition(self):
        """Test addition of positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(100, 0), 100)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        """Test subtraction of various numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # --- Multiplication Tests ---
    def test_multiplication(self):
        """Test multiplication of numbers including zero and negatives."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    # --- Division Tests ---
    def test_division(self):
        """Test division with normal and edge cases."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero check

    def test_division_edge_cases(self):
        """Additional division tests for robustness."""
        self.assertEqual(self.calc.divide(1, -1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333, places=4)
        self.assertIsNone(self.calc.divide(0, 0))  # both are zero


if __name__ == '__main__':
    unittest.main()
