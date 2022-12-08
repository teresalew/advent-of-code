import pathlib
import string
from collections import Counter

PUZZLE_DIR = pathlib.Path(__file__).parent

EXAMPLE_1_INPUT = pathlib.Path(PUZZLE_DIR, "example1.txt")
INPUT = pathlib.Path(PUZZLE_DIR, "input.txt")

# Set up priority map
ALPHABET = list(string.ascii_letters)
PRIORITIES = [i for i in range(1, 53)]
PRIORITY_MAP = {ALPHABET[i]: PRIORITIES[i] for i in range(len(ALPHABET))}


def find_common_item(string1, string2):
    string1_map = Counter(string1)
    string2_map = Counter(string2)

    for key in string1_map:
        for key2 in string2_map:
            if key == key2:
                return key


def find_common_item_2(string1, string2, string3):
    string1_map = Counter(string1)
    string2_map = Counter(string2)
    string3_map = Counter(string3)

    for key in string1_map:
        for key2 in string2_map:
            for key3 in string3_map:
                if key == key2 == key3:
                    return key


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input, mode="rt") as f:
        lines = f.read().split("\n")
    return lines


def part1(data):
    """Solve part 1."""
    rucksacks = []
    for line in data:
        first, second = line[:len(line)//2], line[len(line)//2:]
        rucksacks.append([first, second])

    total_sum = 0
    for rucksack in rucksacks:
        first, second = rucksack
        common_item = find_common_item(first, second)
        total_sum += PRIORITY_MAP[common_item]
    return total_sum


def part2(data):
    """Solve part 2."""
    rucksack_groups = []
    step = 3
    for i in range(0, len(data), step):
        x = i
        rucksack_groups.append(data[x:x+step])

    total_sum = 0
    for rucksack in rucksack_groups:
        first, second, third = rucksack
        common_item = find_common_item_2(first, second, third)
        total_sum += PRIORITY_MAP[common_item]
    return total_sum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


print(solve(INPUT))
