import pytest
from roman_numerals import RomanNumerals


_INT_ROMAN_PAIRS = [
    (1000, 'M'),
    (21, 'XXI'),
    (2008, 'MMVIII'),
    (1990, 'MCMXC')
]


@pytest.mark.parametrize("int_, expected_roman", _INT_ROMAN_PAIRS)
def test_to_roman(int_, expected_roman):
    assert RomanNumerals.to_roman(int_) == expected_roman


@pytest.mark.parametrize("roman, expected_int",
                         [x[::-1] for x in _INT_ROMAN_PAIRS])
def test_from_roman(roman, expected_int):
    assert RomanNumerals.from_roman(roman) == expected_int
