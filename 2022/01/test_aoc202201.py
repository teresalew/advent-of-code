import pathlib
import pytest
import aoc202201 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent
EXAMPLE_1_INPUT = pathlib.Path(PUZZLE_DIR, "example1.txt")
INPUT = pathlib.Path(PUZZLE_DIR, "input.txt")


@pytest.fixture
def example1():
    return aoc.parse(EXAMPLE_1_INPUT)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [[1000, 2000, 3000], [4000], [5000,6000], [7000, 8000, 9000], [10000]]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 24000


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 45000
