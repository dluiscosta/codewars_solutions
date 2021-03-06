import pytest
from get_smallest_bigger_int_with_same_digits \
    import get_smallest_bigger_int_with_same_digits


TEST_CASES = [
    (6, -1),
    (12, 21),
    (2017, 2071),
    (531, -1),
    (1977, 7179),
    (1234567890, 1234567908),
    (3998877665544332211, 4112233345566778899)
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize('int_, expected_sbiwsd', TEST_CASES)
def test_get_smallest_bigger_int_with_same_digits(int_, expected_sbiwsd):
    assert get_smallest_bigger_int_with_same_digits(int_) == expected_sbiwsd
