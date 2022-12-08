import pathlib
import pytest
import aoc202204 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent
EXAMPLE_1_INPUT = pathlib.Path(PUZZLE_DIR, "example1.txt")
INPUT = pathlib.Path(PUZZLE_DIR, "input.txt")


@pytest.fixture
def example1():
    return aoc.parse(EXAMPLE_1_INPUT)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
      [['2', '4'], ['6', '8']],
      [['2', '3'], ['4', '5']],
      [['5', '7'], ['7', '9']],
      [['2', '8'], ['3', '7']],
      [['6', '6'], ['4', '6']],
      [['2', '6'], ['4', '8']]
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 2


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 4
