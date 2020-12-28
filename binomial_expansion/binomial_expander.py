import re


class BinomialExpander:

    _EXPR_REGEX = re.compile(
        r"\((?P<a>\-?[0-9]*)(?P<x>[a-z])\+?(?P<b>\-?[0-9]+)\)\^(?P<n>[0-9]+)"
    )
    _A_EXCEPTIONS = {'': 1, '-': -1}

    _memorized_pascals_triangle_rows = [[1]]

    @classmethod
    def _extract_variables(cls, expr):
        match = re.fullmatch(cls._EXPR_REGEX, expr)
        if not match:
            raise ValueError('Invalid expression {}.'.format(expr))
        a = match.group('a')
        return (
            int(a) if a not in cls._A_EXCEPTIONS else cls._A_EXCEPTIONS[a],
            int(match.group('b')), match.group('x'), int(match.group('n'))
        )

    @classmethod
    def _get_pascals_triangle_row(cls, n):
        if n < len(cls._memorized_pascals_triangle_rows):
            return cls._memorized_pascals_triangle_rows[n]
        else:
            previous_row = cls._get_pascals_triangle_row(n-1)
            row = [a+b for a, b in zip([0]+previous_row, previous_row+[0])]
            cls._memorized_pascals_triangle_rows.append(row)
            return row

    @staticmethod
    def _build_polinomial(a, b, x, n, coeffs):
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

    @classmethod
    def expand(cls, expr):
        a, b, x, n = cls._extract_variables(expr)
        coeffs = cls._get_pascals_triangle_row(n)
        return cls._build_polinomial(a, b, x, n, coeffs)


expand = BinomialExpander.expand  # for Codewars
