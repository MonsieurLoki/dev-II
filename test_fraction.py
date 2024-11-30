from fraction import Fraction

def test_fraction():
    # Création de quelques fractions
    f1 = Fraction(3, 4)
    f2 = Fraction(-5, 6)
    f3 = Fraction(2, 1)
    f4 = Fraction(0, 5)
    print(f"f1: {f1}, f2: {f2}, f3: {f3}, f4: {f4}")

    # Simplification
    f5 = Fraction(10, -20)
    print(f"f5 simplifiée: {f5}")

    # Opérations arithmétiques
    print(f"f1 + f2 = {f1 + f2}")
    print(f"f1 - f2 = {f1 - f2}")
    print(f"f1 * f2 = {f1 * f2}")
    print(f"f1 / f2 = {f1 / f2}")
    print(f"f1 ** 2 = {f1 ** 2}")

    # Propriétés
    print(f"f1 est zéro: {f1.is_zero()}")
    print(f"f4 est zéro: {f4.is_zero()}")
    print(f"f3 est un entier: {f3.is_integer()}")
    print(f"f1 est propre: {f1.is_proper()}")
    print(f"f1 est une fraction unitaire: {f1.is_unit()}")

    # Comparaisons
    print(f"f1 == Fraction(6, 8): {f1 == Fraction(6, 8)}")
    print(f"f1 est adjacent à f2: {f1.is_adjacent_to(Fraction(1, 4))}")

    # Négatif et valeur absolue
    print(f"Négation de f1: {-f1}")
    print(f"Valeur absolue de f2: {abs(f2)}")

if __name__ == "__main__":
    test_fraction()
