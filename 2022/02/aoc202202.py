import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

EXAMPLE_1_INPUT = pathlib.Path(PUZZLE_DIR, "example1.txt")
INPUT = pathlib.Path(PUZZLE_DIR, "input.txt")

SCORES = {
    'X': 1, #rock
    'Y': 2, #paper
    'Z': 3, #scissors
}

OUTCOMES = {
    'win': 6,
    'lose': 0,
    'draw': 3,
}


def determine_outcome(play):
    if play in ['AY', 'BZ', 'CX']:  # rock/paper, paper/scissor, scissor/rock
        return 'win'
    elif play in ['AZ', 'BX', 'CY']: # rock/scissor, paper/rock, scissor/paper
        return 'lose'
    else:
        return 'draw'


def determine_outcome2(player2):
    if player2 == 'X':
        return 'lose'
    elif player2 == 'Y':
        return 'draw'
    else:
        return 'win'


def determine_player2_points(player1, outcome):
    if player1 == 'A': #rock
        if outcome == 'draw': #rock
            return 1
        elif outcome == 'win': #paper
            return 2
        else:
            return 3 # scissors
    elif player1 == 'B': #paper
        if outcome == 'draw': #paper
            return 2
        elif outcome == 'win': #scissors
            return 3
        else: #rock
            return 1
    else: #scissors
        if outcome == 'draw': #scissors
            return 3
        elif outcome == 'win': #rock
            return 1
        else: #paper
            return 2


def parse(puzzle_input):
    """Parse input."""
    with open(puzzle_input, mode="rt") as f:
        lines = f.read().split("\n")
    parsed_input = [line.split(" ") for line in lines]
    return parsed_input


def part1(data):
    """Solve part 1."""
    total_score = 0
    for round in data:
        round_score = 0
        player1, player2 = round
        player2_points = SCORES[player2]
        outcome = determine_outcome(''.join(round))
        round_score = player2_points + OUTCOMES[outcome]
        total_score += round_score
    return total_score


def part2(data):
    """Solve part 2."""
    total_score = 0

    for round in data:
        round_score = 0
        player1, desired_outcome = round
        outcome = determine_outcome2(desired_outcome)
        player2_points = determine_player2_points(player1, outcome)
        round_score = player2_points + OUTCOMES[outcome]
        total_score += round_score

    return total_score


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

# print(determine_outcome('AY') == 'win')
# print(determine_outcome('BX') == 'lose')
# print(determine_outcome('CZ') == 'draw')

# print(get_player2_points('Y') == 2)
# print(get_player2_points('X') == 1)
# print(get_player2_points('Z') == 3)

print(solve(INPUT))
