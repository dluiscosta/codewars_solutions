import pytest
from faberg_easter_eggs_crush_utilitary import FabergEasterEggsCrushUtilitary

MAX_SKYSCRAPPER_HEIGHT_WITH_DETERMINABLE_TARGET_FLOOR_TEST_CASES = [
    (0, 14, 0),
    (2, 0, 0),
    (2, 14, 105),
    (7, 20, 137979),
    (7, 500, 1507386560013475),
    (237, 500, int(
        '431322842186730691997112653891062105065260343258332219390917925258990'
        '318721206767477889789852729810256244129132212314387344900067338552484'
        '172804802659'
    )),
    (477, 500, int(
        '327339060789614187001318969682759915221664204604306478948329136809613'
        '379640467455488327009232590415715088668412742095986665893957843642534'
        '2102468327399'
    ))
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
