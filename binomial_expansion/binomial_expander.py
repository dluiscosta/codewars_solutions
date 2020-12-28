class BinomialExpander:

    @staticmethod
    def _extract_variables(expr):
        raise NotImplementedError()

    @staticmethod
    def _get_pascals_triangle_row(n_choices):
        raise NotImplementedError()

    @staticmethod
    def _build_polinomial(a, b, x, coeffs):
        raise NotImplementedError()

    @classmethod
    def expand(cls, expr):
        a, b, x, n = cls._extract_variables(expr)
        coeffs = cls._get_pascals_triangle_row(n)
        return cls._build_polinomial(a, b, x, coeffs)
