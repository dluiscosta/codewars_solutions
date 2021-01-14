import pytest
from faberg_easter_eggs_crush_utilitary import FabergEasterEggsCrushUtilitary

MAX_SKYSCRAPPER_HEIGHT_WITH_DETERMINABLE_TARGET_FLOOR_TEST_CASES = [
    (0, 14, 0),
    (2, 0, 0),
    (2, 14, 105),
    (7, 20, 137979)
]  # each tuple consists of (eggs, tries, expected_return)


@pytest.mark.parametrize(
    'eggs, tries, expected_return',
    MAX_SKYSCRAPPER_HEIGHT_WITH_DETERMINABLE_TARGET_FLOOR_TEST_CASES
)
def test_max_skyscrapper_height_with_determinable_target_floor(
        eggs, tries, expected_return):
    assert FabergEasterEggsCrushUtilitary.\
        max_skyscrapper_height_with_determinable_target_floor(eggs, tries) == \
        expected_return
