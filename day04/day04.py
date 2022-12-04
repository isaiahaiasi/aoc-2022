import sys


def get_pair_data(input):
    pairs = []
    for a, b in [pair.split(',') for pair in input]:
        a1, a2 = map(int, a.split('-'))
        b1, b2 = map(int, b.split('-'))
        pairs.append([[a1, a2], [b1, b2]])
    return pairs


def is_range_contained(a1, a2, b1, b2):
    return (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2)


def is_range_overlapping(a1, a2, b1, b2):
    return (a1 <= b1 and a2 >= b1) or (b1 <= a1 and b2 >= a1)


def load_input(path):
    lines = []
    with open(path, "r") as fp:
        for line in fp:
            lines.append(line.strip())
    return lines


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    input = load_input(path)

    contained_count = overlapping_count = 0
    for [a1, a2], [b1, b2] in get_pair_data(input):
        contained_count += int(is_range_contained(a1, a2, b1, b2))
        overlapping_count += int(is_range_overlapping(a1, a2, b1, b2))

    print('contained:', contained_count)
    print('overlapping:', overlapping_count)


if __name__ == "__main__":
    main()
