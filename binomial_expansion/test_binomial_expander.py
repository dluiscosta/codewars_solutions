import pytest
from binomial_expander import BinomialExpander


PASCALS_TRIANGLE_ROWS = {
    '0': [1],
    '3': [1, 3, 3, 1],
    '7': [1, 7, 21, 35, 35, 21, 7, 1]
}
VALID_TEST_CASES = {
    '(x+1)^2': {
        'variables': (1, 1, 'x', 2),
        'expanded': 'x^2+2x+1'
    },
    '(-x+1)^2': {
        'variables': (-1, 1, 'x', 2),
        'expanded': 'x^2-2x+1'
    },
    '(7x-7)^0': {
        'variables': (7, -7, 'x', 0),
        'expanded': '1'
    },
    '(5m+3)^4': {
        'variables': (5, 3, 'm', 4),
        'expanded': '625m^4+1500m^3+1350m^2+540m+81'
    },
    '(2x-3)^3': {
        'variables': (2, -3, 'x', 3),
        'expanded': '8x^3-36x^2+54x-27'
    },
    '(-5m+3)^4': {
        'variables': (-5, 3, 'm', 4),
        'expanded': '625m^4-1500m^3+1350m^2-540m+81'
    },
    '(-2k-3)^3': {
        'variables': (-2, -3, 'k', 3),
        'expanded': '-8k^3-36k^2-54k-27'
    }
}


@pytest.mark.parametrize('expr, expected_variables', [
    pytest.param(expr, expected['variables'], id=expr)
    for expr, expected in VALID_TEST_CASES.items()
])
def test__extract_variables(expr, expected_variables):
    assert BinomialExpander._extract_variables(expr) == expected_variables


@pytest.mark.parametrize('row_n, expected_row', [
    pytest.param(int(row_n), expected_row, id=row_n)
    for row_n, expected_row in PASCALS_TRIANGLE_ROWS.items()
])
def test__get_pascals_triangle_row(row_n, expected_row):
    assert BinomialExpander._get_pascals_triangle_row(row_n) == expected_row


@pytest.mark.parametrize('expr, expected_expanded', [
    pytest.param(
        expr, expected['expanded'], id=expr,
        marks=pytest.mark.depends(on=[
            f'test__extract_variables[{expr}]',
            'test__get_pascals_triangle_row'
        ])
    )
    for expr, expected in VALID_TEST_CASES.items()
])
def test_expand(expr, expected_expanded):
    assert BinomialExpander.expand(expr) == expected_expanded
