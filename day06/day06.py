import sys


def find_marker(input, marker_len=4):
    for i in range(marker_len, len(input)):
        if len(set(input[i - marker_len:i])) == marker_len:
            return i


def load_input(path):
    with open(path, "r") as fp:
        return fp.read()


input = load_input(sys.argv[1] if len(sys.argv) > 1 else 'input.txt')
print('result:', find_marker(input, 14))
