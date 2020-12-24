from itertools import groupby


class RomanNumerals:
    ROMAN_TO_INT = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    INT_TO_ROMAN = {v: k for k, v in ROMAN_TO_INT.items()}
    FIRST_ROMANS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    @classmethod
    def _break_into_partials(cls, int_):
        """Return a list of tuples (d, e) representing integers smaller or
        divisible by 10 (value = d*10**e), where their sum equals 'int_'"""
        int_str = str(int_)
        return [(int(digit), len(int_str)-pos-1)
                for pos, digit in enumerate(int_str) if digit != '0']

    @classmethod
    def _partial_to_roman(cls, digit, exp):
        """Convert the value of digit*10**exp to the roman number system,
        where 'digit' and 'exp' are integers"""
        return ''.join(
            [cls.INT_TO_ROMAN[cls.ROMAN_TO_INT[symb]*10**exp]
             for symb in cls.FIRST_ROMANS[digit]]
        )

    @classmethod
    def to_roman(cls, int_):
        """Convert an integer to the roman number system"""
        partials = cls._break_into_partials(int_)
        return ''.join([cls._partial_to_roman(*part) for part in partials])

    @classmethod
    def from_roman(cls, str_):
        """Convert a number in the roman number system to an integer"""
        symbols, amounts = zip(  # group consecutive identical symbols
            *[(s, sum(1 for s in sl)) for s, sl in groupby(str_)])
        signs = [[1, -1][cls.ROMAN_TO_INT[symb] < cls.ROMAN_TO_INT[next_symb]]
                 for symb, next_symb in zip(symbols, symbols[1:]+symbols[-1:])]
        return sum([cls.ROMAN_TO_INT[symb] * amount * sign
                    for symb, amount, sign in zip(symbols, amounts, signs)])
