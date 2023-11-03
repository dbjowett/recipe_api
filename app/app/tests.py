"""
Sample Tests 
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """Add numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Subtract two numbers"""
        res = calc.subtract(10, 3)

        self.assertEqual(res, 7)

    def test_multiply_numbers(self):
        res = calc.multiply(1, 2)
        self.assertEqual(res, 2)
