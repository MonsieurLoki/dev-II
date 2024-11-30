from math import gcd


class Fraction:
    """Classe représentant une fraction et les opérations associées.

    Auteur : Gaspard Derruine
    Date : Novembre 2024
    Cette classe permet des manipulations et opérations sur les fractions
    """

    def __init__(self, num: int = 0, den: int = 1):
        """Initialise une fraction avec un numérateur et un dénominateur.

        PRE : den != 0
        POST : La fraction est stockée sous sa forme simplifiée avec un dénominateur positif.
        RAISES : ZeroDivisionError si den == 0.
        """
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être égal à zéro.")

        if den < 0:  # On s'assure que le dénominateur est positif
            num, den = -num, -den

        common_divisor = gcd(num, den)
        self._num = num // common_divisor
        self._den = den // common_divisor

    @property
    def numerator(self) -> int:
        """Retourne le numérateur de la fraction."""
        return self._num

    @property
    def denominator(self) -> int:
        """Retourne le dénominateur de la fraction."""
        return self._den

    def __str__(self) -> str:
        """Retourne une représentation textuelle de la fraction sous sa forme simplifiée."""
        return f"{self._num}/{self._den}" if self._den != 1 else f"{self._num}"

    def as_mixed_number(self) -> str:
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte."""
        whole_part = self._num // self._den
        remainder = abs(self._num % self._den)
        if remainder == 0:
            return str(whole_part)
        return f"{whole_part} {remainder}/{self._den}" if whole_part else f"{remainder}/{self._den}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur + pour les fractions."""
        num = self._num * other._den + other._num * self._den
        den = self._den * other._den
        return Fraction(num, den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur - pour les fractions."""
        num = self._num * other._den - other._num * self._den
        den = self._den * other._den
        return Fraction(num, den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur * pour les fractions."""
        return Fraction(self._num * other._num, self._den * other._den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur / pour les fractions."""
        if other._num == 0:
            raise ZeroDivisionError("Division par zéro non autorisée.")
        return Fraction(self._num * other._den, self._den * other._num)

    def __pow__(self, power: int) -> 'Fraction':
        """Surcharge l'opérateur ** pour les fractions."""
        if power < 0:
            return Fraction(self._den ** abs(power), self._num ** abs(power))
        return Fraction(self._num ** power, self._den ** power)

    def __eq__(self, other: 'Fraction') -> bool:
        """Surcharge l'opérateur == pour les fractions."""
        return self._num == other._num and self._den == other._den

    def __float__(self) -> float:
        """Retourne la valeur décimale de la fraction."""
        return self._num / self._den

    def __neg__(self) -> 'Fraction':
        """Retourne la forme négative de la fraction."""
        return Fraction(-self._num, self._den)

    def __abs__(self) -> 'Fraction':
        """Retourne la valeur absolue de la fraction."""
        return Fraction(abs(self._num), self._den)

    def is_zero(self) -> bool:
        """Vérifie si la fraction est égale à zéro."""
        return self._num == 0

    def is_integer(self) -> bool:
        """Vérifie si la fraction est un entier."""
        return self._num % self._den == 0

    def is_proper(self) -> bool:
        """Vérifie si la valeur absolue de la fraction est inférieure à 1."""
        return abs(self._num) < self._den

    def is_unit(self) -> bool:
        """Vérifie si le numérateur de la fraction est égal à 1 sous sa forme simplifiée."""
        return abs(self._num) == 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Vérifie si deux fractions diffèrent d'une fraction unitaire."""
        diff = abs(self - other)
        return diff.numerator == 1 and diff.denominator > 0
