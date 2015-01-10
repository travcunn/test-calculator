import unittest

from calc import Calculator


class AddTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive_integers(self):
        assert self.calculator.add(1, 2) == 3

    def test_add_negative_integers(self):
        assert self.calculator.add(-3, -4) == -7

    def test_add_negative_and_positive_integers(self):
        assert self.calculator.add(-4, 5) == 1
        
 
class SubtractTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_sub_positive_int(self):
        assert self.calculator.sub(2, 1) == 1

    def test_sub_negative_int(self):
		assert self.calculator.sub(-2, -2) == 0

    def test_sub_negative_and_positive_int(self):
        assert self.calculator.sub(-4, 5) == -9


if __name__ == "__main__":
    unittest.main()
