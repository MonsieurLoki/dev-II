from fraction import Fraction
import unittest
import coverage


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
        self.assertFalse(Fraction(3, 4).is_adjacent_to(Fraction(7, 4)))
        self.assertTrue(Fraction(3, 4).is_adjacent_to(Fraction(2, 3)))


if __name__ == "__main__":
    # Initialisation de la couverture
    cov = coverage.Coverage()
    cov.start()

    # Exécution des tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    # Arrêt de la couverture
    cov.stop()

    # Génération du rapport
    print("\nRapport de couverture :\n")
    cov.report()  # Affiche dans le terminal
    cov.html_report(directory="htmlcov")  # Génère un rapport HTML dans le dossier "htmlcov"
    print("\nRapport HTML généré dans le dossier 'htmlcov'.")
