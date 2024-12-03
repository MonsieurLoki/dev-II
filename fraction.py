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
        """Retourne le numérateur de la fraction.

        PRE : /
        POST : Retourne un entier correspondant au numérateur.
        """
        return self._num

    @property
    def denominator(self) -> int:
        """Retourne le dénominateur de la fraction.

        PRE : /
        POST : Retourne un entier positif correspondant au dénominateur.
        """
        return self._den
        
    # ------------------ Textual representations ------------------

    def __str__(self) -> str:
        """Retourne une représentation textuelle de la fraction sous sa forme simplifiée.

        PRE : /
        POST : Retourne une chaîne de caractères au format "num/den" ou "num" si le dénominateur vaut 1.
        """
        return f"{self._num}/{self._den}" if self._den != 1 else f"{self._num}"

    def as_mixed_number(self) -> str:
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte.

        PRE : /
        POST : Retourne une chaîne de caractères indiquant la partie entière et le reste.
        """
        whole_part = self._num // self._den
        remainder = abs(self._num % self._den)
        if remainder == 0:
            return str(whole_part)
        return f"{whole_part} {remainder}/{self._den}" if whole_part else f"{remainder}/{self._den}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur + pour les fractions.

        PRE : other est une instance de Fraction.
        POST : Retourne une nouvelle fraction représentant la somme des deux fractions.
        """
        num = self._num * other._den + other._num * self._den
        den = self._den * other._den
        return Fraction(num, den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur - pour les fractions.

        PRE : other est une instance de Fraction.
        POST : Retourne une nouvelle fraction représentant la différence des deux fractions.
        """
        num = self._num * other._den - other._num * self._den
        den = self._den * other._den
        return Fraction(num, den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur * pour les fractions.

        PRE : other est une instance de Fraction.
        POST : Retourne une nouvelle fraction représentant le produit des deux fractions.
        """
        return Fraction(self._num * other._num, self._den * other._den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """Surcharge l'opérateur / pour les fractions.

        PRE : other est une instance de Fraction dont le numérateur est différent de zéro.
        POST : Retourne une nouvelle fraction représentant la division des deux fractions.
        RAISES : ZeroDivisionError si le numérateur de other est égal à 0.
        """
        if other._num == 0:
            raise ZeroDivisionError("Division par zéro non autorisée.")
        return Fraction(self._num * other._den, self._den * other._num)

    def __pow__(self, power: int) -> 'Fraction':
        """Surcharge l'opérateur ** pour les fractions.

        PRE : power est un entier.
        POST : Retourne une nouvelle fraction représentant la fraction élevée à la puissance donnée.
        """
        if power < 0:
            return Fraction(self._den ** abs(power), self._num ** abs(power))
        return Fraction(self._num ** power, self._den ** power)

    def __eq__(self, other: 'Fraction') -> bool:
        """Surcharge l'opérateur == pour les fractions.

        PRE : other est une instance de Fraction.
        POST : Retourne True si les deux fractions sont équivalentes, False sinon.
        """
        return self._num == other._num and self._den == other._den

    def __float__(self) -> float:
        """Retourne la valeur décimale de la fraction.

        PRE : /
        POST : Retourne un float représentant la valeur de la fraction.
        """
        return self._num / self._den

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Vérifie si la fraction est égale à zéro.

        PRE : /
        POST : Retourne True si la fraction est égale à zéro, False sinon.
        """
        return self._num == 0

    def is_integer(self) -> bool:
        """Vérifie si la fraction est un entier.

        PRE : /
        POST : Retourne True si la fraction est un entier, False sinon.
        """
        return self._num % self._den == 0

    def is_proper(self) -> bool:
        """Vérifie si la valeur absolue de la fraction est inférieure à 1.

        PRE : /
        POST : Retourne True si la valeur absolue de la fraction est inférieure à 1, False sinon.
        """
        return abs(self._num) < self._den

    def is_unit(self) -> bool:
        """Vérifie si le numérateur de la fraction est égal à 1 sous sa forme simplifiée.

        PRE : /
        POST : Retourne True si le numérateur est égal à 1, False sinon.
        """
        return abs(self._num) == 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Vérifie si deux fractions diffèrent d'une fraction unitaire.

        PRE : other est une instance de Fraction.
        POST : Retourne True si la différence absolue entre les deux fractions est une fraction unitaire.
        """
        diff = self - other
        return diff.numerator == 1 and diff.denominator > 0
