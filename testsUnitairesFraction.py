from fraction import Fraction
import unittest
import coverage


class TestFraction(unittest.TestCase):

    def test_constructor(self):
        """Test du constructeur pour différentes valeurs."""
        self.assertEqual(Fraction(10, 20), Fraction(1, 2))  # Simplification
        self.assertEqual(Fraction(-4, 8), Fraction(-1, 2))  # Gestion des signes
        self.assertEqual(Fraction(-4, -8), Fraction(1, 2))  # Signes négatifs
        self.assertEqual(Fraction(0, 1), Fraction(0, 1))  # Numérateur zéro
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)  # Dénominateur nul

    def test_str(self):
        """Test de la représentation textuelle."""
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(3, 1)), "3")
        self.assertEqual(str(Fraction(-3, 4)), "-3/4")
        self.assertEqual(str(Fraction(0, 1)), "0")

    def test_as_mixed_number(self):
        """Test de la conversion en nombre mixte."""
        self.assertEqual(Fraction(5, 3).as_mixed_number(), "1 2/3")
        self.assertEqual(Fraction(6, 3).as_mixed_number(), "2")
        self.assertEqual(Fraction(1, 3).as_mixed_number(), "1/3")

    def test_add(self):
        """Test de l'addition de fractions."""
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(-1, 2) + Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(0, 1) + Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(Fraction(-3, 4) + Fraction(3, 4), Fraction(0, 1))

    def test_sub(self):
        """Test de la soustraction de fractions."""
        self.assertEqual(Fraction(3, 4) - Fraction(1, 4), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(-1, 2) - Fraction(-1, 3), Fraction(-1, 6))

    def test_mul(self):
        """Test de la multiplication de fractions."""
        self.assertEqual(Fraction(1, 2) * Fraction(2, 3), Fraction(1, 3))
        self.assertEqual(Fraction(-1, 2) * Fraction(2, 3), Fraction(-1, 3))
        self.assertEqual(Fraction(0, 1) * Fraction(3, 4), Fraction(0, 1))

    def test_truediv(self):
        """Test de la division de fractions."""
        self.assertEqual(Fraction(1, 2) / Fraction(1, 3), Fraction(3, 2))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)

    def test_pow(self):
        """Test de l'élévation à une puissance."""
        self.assertEqual(Fraction(2, 3) ** 2, Fraction(4, 9))
        self.assertEqual(Fraction(2, 3) ** -1, Fraction(3, 2))
        self.assertEqual(Fraction(2, 3) ** 0, Fraction(1, 1))
        self.assertEqual(Fraction(-1, 2) ** 3, Fraction(-1, 8))  # Impair négatif

    def test_eq(self):
        """Test de l'égalité entre fractions."""
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(2, 3))
        self.assertTrue(Fraction(0, 1) == Fraction(0, 5))

    def test_is_zero(self):
        """Test si une fraction est égale à zéro."""
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

    def test_is_integer(self):
        """Test si une fraction est un entier."""
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(5, 3).is_integer())

    def test_is_proper(self):
        """Test si une fraction est propre."""
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())

    def test_is_unit(self):
        """Test si une fraction est unitaire."""
        self.assertTrue(Fraction(1, 2).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_is_adjacent_to(self):
        """Test si deux fractions sont adjacentes."""
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))
        self.assertFalse(Fraction(1, 2).is_adjacent_to(Fraction(1, 4)))

    def test_float(self):
        """Test de la conversion en float."""
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(3, 4)), 0.75)
        self.assertEqual(float(Fraction(-1, 3)), -1 / 3)


if __name__ == '__main__':
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
