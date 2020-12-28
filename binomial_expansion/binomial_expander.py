import re


class BinomialExpander:

    _EXPR_REGEX = re.compile(
        r"\((?P<a>\-?[0-9]*)(?P<x>[a-z])\+?(?P<b>\-?[0-9]+)\)\^(?P<n>[0-9]+)"
    )
    _memorized_pascals_triangle_rows = [[1]]

    @classmethod
    def _extract_variables(cls, expr):
        match = re.fullmatch(cls._EXPR_REGEX, expr)
        if not match:
            raise ValueError('Invalid expression {}.'.format(expr))
        return (
            int(match.group('a')) if match.group('a') else 1,
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
    def _build_polinomial(a, b, x, coeffs):
        raise NotImplementedError()

    @classmethod
    def expand(cls, expr):
        a, b, x, n = cls._extract_variables(expr)
        coeffs = cls._get_pascals_triangle_row(n)
        return cls._build_polinomial(a, b, x, coeffs)
