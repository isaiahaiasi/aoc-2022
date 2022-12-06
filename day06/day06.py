import sys
from collections import deque


def find_marker(input, marker_len=4):
    s = deque(input[0:marker_len])
    for i in range(marker_len, len(input)):
        if len(set(s)) == marker_len:
            return i
        s.append(input[i])
        s.popleft()
    return None


def load_input(path):
    with open(path, "r") as fp:
        return fp.read()


input = load_input(sys.argv[1] if len(sys.argv) > 1 else 'input.txt')
print('result:', find_marker(input, 14))
