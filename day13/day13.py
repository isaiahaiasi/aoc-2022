import sys
from functools import cmp_to_key


def sort_packet(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(right), len(left))):
            result = sort_packet(left[i], right[i])
            if result != 0:
                return result
        return sort_packet(len(left), len(right))
    elif isinstance(left, list):
        return sort_packet(left, [right])
    elif isinstance(right, list):
        return sort_packet([left], right)
    else:
        # int <=> int
        diff = right - left
        return 0 if diff == 0 else diff/abs(diff)


def part_1(pairs):
    res_sum = 0
    for i, pair in enumerate(pairs):
        if sort_packet(*pair) == 1:
            res_sum += i + 1
    return res_sum


def part_2(data):
    data = data + [[[2]]] + [[[6]]]
    data = sorted(data, key=cmp_to_key(sort_packet), reverse=True)
    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)


def load_input_1(path):
    with open(path, "r") as fp:
        pairs = fp.read().split('\n\n')
        return [[eval(n) for n in pair.split()] for pair in pairs]


def load_input_2(path):
    with open(path, "r") as fp:
        lines = [line.strip() for line in fp.readlines() if line.strip() != '']
        return [eval(line) for line in lines]


path = sys.argv[1] if len(sys.argv) > 1 else './day13/test-input.txt'

print(f"Part A: {part_1(load_input_1(path))}")
print(f"Part B: {part_2(load_input_2(path))}")


# how many pairs of packets are in the right order?
# first in pair LEFT, next RIGHT
# if both values are ints, LEFT should be LOWER
# if both are lists, left LIST should run out of items first
# if exactly 1 value is an int, convert int to a list which contains the int, then retry

# PART 1:
# Determine which pairs of packets are already in the right order.
# What is the sum of the indices of those pairs?

# PART 2:
# Ignore pairings
# sort entire set
# Insert 2 new ones: [[2]] [[6]]
# Find the product of their indices after sorting
