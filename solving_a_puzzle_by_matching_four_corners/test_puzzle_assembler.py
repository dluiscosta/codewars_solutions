import pytest
from puzzle_assembler import PuzzleAssembler


ASSEMBLE_TEST_CASES = [
    {
        'test_name': "example_test",
        'width': 3,
        'height': 3,
        'expected_assembled_puzzle': [(7, 6, 4), (8, 5, 2), (3, 1, 9)],
        'pieces':
            [((None, 5), (None, None), 3), ((17, None), (None, None), 9),
             ((None, 4), (None, 5), 8), ((4, 11), (5, 17), 5),
             ((11, None), (17, None), 2), ((None, None), (None, 4), 7),
             ((5, 17), (None, None), 1), ((None, None), (11, None), 4),
             ((None, None), (4, 11), 6)],
    },
    {
        'test_name': "fixed_test01",
        'width': 2,
        'height': 3,
        'expected_assembled_puzzle': [(2, 4), (3, 1), (5, 6)],
        'pieces':
            [((None, None), (None, 8), 2), ((None, 8), (None, 21), 3),
             ((8, None), (21, None), 1), ((21, None), (None, None), 6),
             ((None, 21), (None, None), 5), ((None, None), (8, None), 4)],
    },
    {
        'test_name': "fixed_test02",
        'width': 5,
        'height': 4,
        'expected_assembled_puzzle':
            [(18, 4, 3, 16, 15), (19, 10, 7, 6, 17), (5, 1, 20, 12, 11),
             (14, 8, 2, 9, 13)],
        'pieces':
            [((10, 11), (17, 2), 12), ((None, 3), (None, 5), 5),
             ((None, None), (None, 18), 18), ((1, 6), (10, 11), 6),
             ((7, 1), (12, 10), 7), ((18, 7), (3, 12), 10),
             ((17, 2), (None, None), 9), ((11, None), (2, None), 11),
             ((None, 18), (None, 3), 19), ((None, None), (6, None), 15),
             ((None, None), (18, 7), 4), ((None, None), (1, 6), 16),
             ((None, 5), (None, None), 14), ((5, 8), (None, None), 8),
             ((12, 10), (8, 17), 20), ((3, 12), (5, 8), 1),
             ((6, None), (11, None), 17), ((None, None), (7, 1), 3),
             ((2, None), (None, None), 13), ((8, 17), (None, None), 2)],
    }
]


@pytest.mark.timeout(1)
@pytest.mark.parametrize('test_case', ASSEMBLE_TEST_CASES,
                         ids=[tc['test_name'] for tc in ASSEMBLE_TEST_CASES])
def test_assemble(test_case):
    assert PuzzleAssembler.assemble(
        test_case['pieces'], test_case['width'], test_case['height']
    ) == test_case['expected_assembled_puzzle']
