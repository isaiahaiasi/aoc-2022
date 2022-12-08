import sys


class Solver:
    def __init__(self, input):
        self.forest = input
        self.rotated_forest = list(zip(*input))
        self.height = len(input)
        self.width = len(input[0])

    def is_exterior(self, x, y):
        return not (
            x < self.height - 1
            and y < self.width - 1
            and x >= 1
            and y >= 1
        )

    def is_visible(self, x, y):
        return min(
            max(self.forest[y][0:x]),
            max(self.forest[y][x + 1:self.width]),
            max(self.rotated_forest[x][0:y]),
            max(self.rotated_forest[x][y + 1:self.height])
        ) < self.forest[y][x]

    def visible_count(self):
        vis = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.is_exterior(i, j) or self.is_visible(i, j):
                    vis += 1
        return vis

    def best_local_visibility(self):
        best = 0
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                score = 1
                for v, h in dirs:
                    step = 0
                    while True:
                        step += 1
                        y = i + (v * step)
                        x = j + (h * step)
                        if (self.is_exterior(x, y) or self.forest[y][x] >= self.forest[i][j]):
                            break
                    score *= step
                best = max(best, score)
        return best


def load_input(path):
    with open(path, "r") as fp:
        return [[int(n) for n in list(line.strip())] for line in fp]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'day08/test-input.txt'
    input = load_input(path)

    solver = Solver(input)

    print('part A:', solver.visible_count())
    print('part B:', solver.best_local_visibility())


if __name__ == "__main__":
    main()
