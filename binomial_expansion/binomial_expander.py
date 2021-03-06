"""
Solution to the problem Binomial Expansion (3kyu) of Code Wars.
Description:
    The purpose of this kata is to write a program that can do some algebra.
    Write a function expand that takes in an expresion with a single, one
    character variable, and expands it. The expresion is in the form (ax+b)^n
    where a and b are integers which may be positive or negative, x is any one
    character long variable, and n is a natural number. If a = 1, no coeficient
    will be placed in front of the variable. If a = -1, a "-" will be placed in
    front of the variable.
    The expanded form should be returned as a string in the form
    ax^b+cx^d+ex^f... where a, c, and e are the coefficients of the term, x is
    the original one character variable that was passed in the original
    expression and b, d, and f, are the powers that x is being raised to in
    each term and are in decreasing order. If the coeficient of a term is zero,
    the term should not be included. If the coeficient of a term is one, the
    coeficient should not be included. If the coeficient of a term is -1, only
    the "-" should be included. If the power of the term is 0, only the
    coeficient should be included. If the power of the term is 1, the carrot
    and power should be excluded.
"""

import re
from abc import ABC


class BinomialExpander(ABC):
    """Wrapper for the method 'expand' and it's utilities"""

    _EXPR_REGEX = re.compile(
        r"\((?P<a>\-?[0-9]*)(?P<x>[a-z])\+?(?P<b>\-?[0-9]+)\)\^(?P<n>[0-9]+)"
    )
    _A_EXCEPTIONS = {'': 1, '-': -1}

    _memorized_pascals_triangle_rows = [[1]]

    # O(len(expr)) time and space
    @classmethod
    def _extract_variables(cls, expr: str) -> tuple:
        """Extract the variables a, b, x and n from a mathematical expression
        of the form (ax+b)^n"""
        match = re.fullmatch(cls._EXPR_REGEX, expr)
        if not match:
            raise ValueError('Invalid expression {}.'.format(expr))
        a = match.group('a')
        return (
            int(a) if a not in cls._A_EXCEPTIONS else cls._A_EXCEPTIONS[a],
            int(match.group('b')), match.group('x'), int(match.group('n'))
        )

    # O(n) time and space
    @classmethod
    def _get_pascals_triangle_row(cls, n: int) -> list:
        """Get the nth row of the Pascal's triangle, starting from 0"""
        if n < len(cls._memorized_pascals_triangle_rows):
            return cls._memorized_pascals_triangle_rows[n]
        else:
            previous_row = cls._get_pascals_triangle_row(n-1)
            row = [a+b for a, b in zip([0]+previous_row, previous_row+[0])]
            cls._memorized_pascals_triangle_rows.append(row)
            return row

    # O(n) time and space
    @classmethod
    def _build_polynomial(cls, a: int, b: int, x: str, n: int) -> str:
        """Build a polynomial that equals (ax+b)^n"""
        coeffs = cls._get_pascals_triangle_row(n)
        terms = []
        for i, coeff in enumerate(coeffs):
            coeff_ = coeff*a**(n-i)*b**i
            if coeff_ != 0:
                terms.append('{}{}'.format(
                    str(coeff_) if coeff_ not in [1, -1] else str(coeff_)[:-1],
                    x + '^' + str(n-i) if n-i > 1 else ('', x)[n-i]
                ) if not (coeff_ in [1, -1] and n-i == 0) else str(coeff_))
        return ''.join(['+' + term if term[0] != '-' and i != 0 else term
                        for i, term in enumerate(terms)])

    # O(len(expr) + n) time and space
    @classmethod
    def expand(cls, expr: str) -> str:
        """
        Expand a mathematical expression of the form (ax+b)^n.

        Expand a power of a binomial, a mathematical expression of the form
        (ax+b)ˆn where 'n' is a natural number, into a polynomial, a sum
        involving terms of the form cxˆd. This method only supports 'a' and 'b'
        integers and 'x' as a lower case 1-letter variable name.

        Parameters
        ----------
        expr : str
            Expression of the form (ax+b)^n.

        Returns
        -------
        str
            The expanded expression, a polynomial.

        """
        a, b, x, n = cls._extract_variables(expr)
        return cls._build_polynomial(a, b, x, n)


expand = BinomialExpander.expand  # for Codewars
