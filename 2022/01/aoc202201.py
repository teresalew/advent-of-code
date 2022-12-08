import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

EXAMPLE_1_INPUT = pathlib.Path(PUZZLE_DIR, "example1.txt")
INPUT = pathlib.Path(PUZZLE_DIR, "input.txt")

def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input, mode="rt") as f:
        elfs = f.read().split("\n\n")
    elfs = [elf.split("\n") for elf in elfs]

    parsed_input = []
    for elf in elfs:
        calories = []
        for calorie in elf:
            calories.append(int(calorie))
        parsed_input.append(calories)

    return parsed_input

def part1(data):
    """Solve part 1."""
    total_calories = []
    for elf in data:
        sum = 0
        for calorie in elf:
            sum += calorie
        total_calories.append(sum)

    return max(total_calories)

def part2(data):
    """Solve part 2."""
    total_calories = []
    for elf in data:
        sum = 0
        for calorie in elf:
            sum += calorie
        total_calories.append(sum)

    total_calories.sort(reverse=True)
    top3_calories = total_calories[:3]

    sum = 0
    for cal in top3_calories:
        sum += cal

    return sum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

print(solve(INPUT))
