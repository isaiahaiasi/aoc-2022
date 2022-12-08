import sys
import re

MAX_SIZE = 100_000
TOTAL_SPACE = 70_000_000
NEED_UNUSED = 30_000_000

dirs = {'/': 0}
dir_stack = ['/']


def add_file(size):
    for d in dir_stack:
        dirs[d] += size


def set_dir_sizes(input):
    for line in input[1:]:
        if line == '$ cd ..':
            dir_stack.pop()
        elif line.startswith('$ cd'):
            dir_name = '/'.join([*dir_stack, line[5:]])
            dir_stack.append(dir_name)
            if not dirs.get(dir_name):
                dirs[dir_name] = 0
        elif re.search('^\d+', line):
            add_file(int(line.split(' ')[0]))


def get_total_size():
    return sum(d for d in dirs.values() if d <= MAX_SIZE)


def get_min_deletion():
    cur_surplus = dirs['/'] + NEED_UNUSED - TOTAL_SPACE
    return min(d for d in dirs.values() if d >= cur_surplus)


def load_input(path):
    with open(path, "r") as fp:
        return [line.strip() for line in fp]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'day07/input.txt'
    input = load_input(path)

    set_dir_sizes(input)

    print('a:', get_total_size())
    print('b:', get_min_deletion())


if __name__ == "__main__":
    main()
