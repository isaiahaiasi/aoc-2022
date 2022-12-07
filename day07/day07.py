import sys

MAX_SIZE = 100_000
TOTAL_SPACE = 70_000_000
NEED_UNUSED = 30_000_000


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def get_size(self):
        return sum(n.get_size() for n in self.children)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class Solver:
    def __init__(self, input):
        self.input = input
        self.root = Dir('/')
        self.cur_dir = self.root
        self.dirs = [self.root]

        self.build()

    def build(self):
        for i, line in enumerate(self.input):
            if line == '$ ls':
                self.ls(i + 1)
            elif line.startswith('$ cd '):
                self.cd(line[5:])

    def cd(self, dir):
        if dir == '/':
            self.cur_dir = self.root
        elif dir == '..':
            self.cur_dir = self.cur_dir.parent
        else:
            self.cur_dir = next(
                (d for d in self.cur_dir.children if d.name == dir)
            )

    def is_cmd(self, line):
        return line == '$ ls' or line.startswith('$ cd ')

    def ls(self, i):
        end_of_output = next(
            (j + i for j, o in enumerate(self.input[i:]) if self.is_cmd(o)),
            len(self.input)
        )
        output = [n.split(' ') for n in self.input[i:end_of_output]]

        for line in output:
            if line[0] == 'dir':
                node = Dir(line[1], self.cur_dir)
                self.cur_dir.children.append(node)
                self.dirs.append(node)  # TODO: bleh
            else:
                self.cur_dir.children.append(File(line[1], int(line[0])))

    def solve_a(self):
        return sum(n.get_size() for n in self.dirs if n.get_size() <= MAX_SIZE)

    def solve_b(self):
        cur_surplus = self.root.get_size() + NEED_UNUSED - TOTAL_SPACE
        return min(d.get_size() for d in self.dirs if d.get_size() >= cur_surplus)


def load_input(path):
    with open(path, "r") as fp:
        return [line.strip() for line in fp]


path = sys.argv[1] if len(sys.argv) > 1 else 'day07/test-input.txt'
input = load_input(path)

solver = Solver(input)

print("part A:", solver.solve_a())
print("part B:", solver.solve_b())
