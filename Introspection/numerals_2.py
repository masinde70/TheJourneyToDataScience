from fractions import Fraction


def mixed_numeral(vulger):

    integer = vulger.numerator // vulger.denominator
    fraction = Fraction(vulger.numerator - integer * vulger.denominator, vulger.denominator)
    return integer, fraction
