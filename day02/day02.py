import sys


class Results:
    LOSE = 0
    TIE = 3
    WIN = 6
    Indexed = [LOSE, TIE, WIN]


# given both hands, give score of result
def get_result_score(theirs, yours):
    hand_differential = yours - theirs
    result = (hand_differential + 1) % 3
    return Results.Indexed[result]


# given opponent's hand & result, get score of your hand
def get_hand_score(op_hand, result):
    # win = 2 -> differential = +1, etc
    hand_differential = result - 1
    return ((op_hand - 1 + hand_differential) % 3) + 1


def get_numeric_round(str_round):
    [str_A, str_X] = str_round.split()
    int_A = ord(str_A) - ord("A") + 1
    int_X = ord(str_X) - ord("X") + 1
    return [int_A, int_X]


def calc_scores_1(rounds):
    score_sum = 0

    for round in rounds:
        [op_hand, your_hand] = get_numeric_round(round)
        result_score = get_result_score(op_hand, your_hand)
        score_sum += result_score + your_hand

    return score_sum


def calc_scores_2(rounds):
    score_sum = 0

    for round in rounds:
        [op_hand, result] = get_numeric_round(round)
        result_score = Results.Indexed[result - 1]
        hand_score = get_hand_score(op_hand, result - 1)
        score_sum += result_score + hand_score

    return score_sum


def load_input(path):
    lines = []
    with open(path, "r") as fp:
        for line in fp:
            lines.append(line.strip())
    return lines


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    input = load_input(path)

    result_1 = calc_scores_1(input)  # -> 13005
    result_2 = calc_scores_2(input)  # -> 11373

    print(result_1, result_2)


if __name__ == "__main__":
    main()
