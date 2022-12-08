import pathlib
import string
from collections import Counter

PUZZLE_DIR = pathlib.Path(__file__).parent

EXAMPLE_1_INPUT = pathlib.Path(PUZZLE_DIR, "example1.txt")
INPUT = pathlib.Path(PUZZLE_DIR, "input.txt")


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input, mode="rt") as f:
        rows = f.read().split("\n")
        pairs = [row.split(",") for row in rows]

        parsed_input = []
        for pair in pairs:
            assignments = []
            for elf in pair:
                assignments.append(elf.split("-"))
            parsed_input.append(assignments)

    return parsed_input



def part1(data):
    """Solve part 1."""
    contained_pairs = 0

    for pairs in data:
        pairs.sort(key=lambda x: int(x[0]))
        start1 = int(pairs[0][0])
        end1 = int(pairs[0][1])
        start2 = int(pairs[1][0])
        end2 = int(pairs[1][1])

        if (start2 <= end1):
            if (
                (end2 <= end1 and start2 >= start1) or
                (start2 == start1 and end2 > end1)
            ):
                contained_pairs += 1

    return contained_pairs



def part2(data):
    """Solve part 2."""
    contained_pairs = 0

    for pairs in data:
        pairs.sort(key=lambda x: int(x[0]))
        start1 = int(pairs[0][0])
        end1 = int(pairs[0][1])
        start2 = int(pairs[1][0])
        end2 = int(pairs[1][1])

        if (start2 <= end1):
            if (end2 <= end1 or start2 >= start1):
                contained_pairs += 1

    return contained_pairs


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


print(solve(INPUT))
