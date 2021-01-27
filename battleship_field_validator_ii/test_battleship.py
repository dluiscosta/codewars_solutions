import pytest
from battleship import Battleship


SHIP_COLLIDES_TEST_CASES = [
    (
        Battleship.Ship((0, 0), 3, Battleship.Ship.Orientation.VERTICAL),
        Battleship.Ship((2, 0), 2, Battleship.Ship.Orientation.VERTICAL),
        True
    ),
    (
        Battleship.Ship((0, 0), 3, Battleship.Ship.Orientation.VERTICAL),
        Battleship.Ship((2, 0), 2, Battleship.Ship.Orientation.HORIZONTAL),
        True
    ),
    (
        Battleship.Ship((0, 0), 3, Battleship.Ship.Orientation.VERTICAL),
        Battleship.Ship((2, 0), 1),
        True
    ),
    (
        Battleship.Ship((0, 0), 3, Battleship.Ship.Orientation.HORIZONTAL),
        Battleship.Ship((0, 2), 1),
        True
    ),
    (
        Battleship.Ship((0, 0), 2, Battleship.Ship.Orientation.VERTICAL),
        Battleship.Ship((2, 0), 2, Battleship.Ship.Orientation.VERTICAL),
        False
    ),
    (
        Battleship.Ship((0, 0), 2, Battleship.Ship.Orientation.VERTICAL),
        Battleship.Ship((2, 0), 2, Battleship.Ship.Orientation.HORIZONTAL),
        False
    ),
    (Battleship.Ship((2, 3), 1), Battleship.Ship((2, 3), 1), True),
    (Battleship.Ship((2, 3), 1), Battleship.Ship((3, 5), 1), False)
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    'ship1, ship2, expected_return',
    [pytest.param(s1, s2, expected, id=str(idx))
     for idx, (s1, s2, expected) in enumerate(SHIP_COLLIDES_TEST_CASES)]
)
def test_ship_collides(ship1, ship2, expected_return):
    assert ship1.collides(ship2) == expected_return


@pytest.mark.timeout(1)
def test__extract_possible_ships():
    field = \
        [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    expected_possible_ships = {
        Battleship.Ship((0, 0), 1),
        Battleship.Ship((0, 0), 2, Battleship.Ship.Orientation.HORIZONTAL),
        Battleship.Ship((0, 0), 3, Battleship.Ship.Orientation.HORIZONTAL),
        Battleship.Ship((0, 1), 1),
        Battleship.Ship((0, 1), 2, Battleship.Ship.Orientation.HORIZONTAL),
        Battleship.Ship((0, 2), 1),
        Battleship.Ship((1, 0), 1),
        Battleship.Ship((0, 0), 2, Battleship.Ship.Orientation.VERTICAL),
    }
    assert Battleship._extract_possible_ships(field) == expected_possible_ships


VALID_FIELDS = [
    ('valid field',
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    ('ships are in contact',
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
         [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
]
INVALID_FIELDS = [
    ('ship parts are missing',
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    ('exceeding number of ships',
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    ("ship parts don't compose a valid set of ships",
        [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
]


@pytest.mark.timeout(10)
@pytest.mark.parametrize('field, expected_return, test_title', [
    pytest.param(field, expected_return, test_title, id=test_title)
    for test_title, field, expected_return in
    [t+(True,) for t in VALID_FIELDS] + [t+(False,) for t in INVALID_FIELDS]
])
def test_validate_field(field, expected_return, test_title):
    assert Battleship.validate_field(field) is expected_return, \
        'Must return {}, {}.'.format(str(expected_return).lower(), test_title)
