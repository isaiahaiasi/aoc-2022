import sys

DIRS = [[0, -1], [0, 1], [-1, 0], [1, 0]]


class Solver:
    def __init__(self, input):
        self.forest = input
        self.z_forest = list(zip(*input))
        self.h = len(input)
        self.w = len(input[0])

    def is_exterior(self, x, y):
        return x >= self.h - 1 or y >= self.w - 1 or x < 1 or y < 1

    def is_visible(self, x, y):
        return (max(self.forest[y][0:x]) < self.forest[y][x]
                or max(self.forest[y][x + 1:self.w]) < self.forest[y][x]
                or max(self.z_forest[x][0:y]) < self.forest[y][x]
                or max(self.z_forest[x][y + 1:self.h]) < self.forest[y][x])

    def visible_count(self):
        vis = 0
        for y in range(self.h):
            for x in range(self.w):
                if self.is_exterior(x, y) or self.is_visible(x, y):
                    vis += 1
        return vis

    def visibility_score(self, y, x):
        score = 1
        for v, h in DIRS:
            step = 0
            while True:
                step += 1
                step_y = y + (v * step)
                step_x = x + (h * step)
                if (self.is_exterior(step_x, step_y)
                        or self.forest[step_y][step_x] >= self.forest[y][x]):
                    break
            score *= step
        return score

    def best_local_visibility(self):
        best = 0
        for i in range(1, self.h - 1):
            for j in range(1, self.w - 1):
                best = max(best, self.visibility_score(i, j))
        return best


def load_input(path):
    with open(path, "r") as fp:
        return [[int(n) for n in list(line.strip())] for line in fp]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'day08/test-input.txt'
    input = load_input(path)

    solver = Solver(input)

    print('part A:', solver.visible_count())  # 1845
    print('part B:', solver.best_local_visibility())  # 230112


if __name__ == "__main__":
    main()
