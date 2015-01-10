import unittest

from calc import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_integers(self):
        assert self.calculator.add(1, 2) == 3

    def test_add_negative_integers(self):
        assert self.calculator.add(-3, -4) == -7

    def test_add_negative_and_positive_integers(self):
        assert self.calculator.add(-4, 5) == 1


if __name__ == "__main__":
    unittest.main()
