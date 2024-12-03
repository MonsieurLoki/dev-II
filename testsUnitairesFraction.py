import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_constructor(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)
        self.assertEqual(Fraction(10, 20), Fraction(1, 2))
        self.assertEqual(Fraction(3, -6), Fraction(-1, 2))

    def test_str(self):
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(3, 1)), "3")

    def test_as_mixed_number(self):
        self.assertEqual(Fraction(5, 3).as_mixed_number(), "1 2/3")
        self.assertEqual(Fraction(6, 3).as_mixed_number(), "2")

    def test_add(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(-1, 2) + Fraction(1, 2), Fraction(0, 1))

    def test_div(self):
        self.assertEqual(Fraction(1, 2) / Fraction(1, 3), Fraction(3, 2))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)

    def test_eq(self):
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(2, 3))

    def test_is_integer(self):
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(5, 3).is_integer())

    def test_is_proper(self):
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_is_adjacent_to(self):
        self.assertFalse(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 6)))


if __name__ == "__main__":
    unittest.main()
