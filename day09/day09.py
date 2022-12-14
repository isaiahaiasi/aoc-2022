import sys


DIRECTION = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move_dir(self, direction):
        x, y = DIRECTION[direction]
        self.x += x
        self.y += y

    @property
    def tup(self):
        return self.x, self.y


class Knot:
    def __init__(self, x, y):
        self.pos = Point(x, y)
        self.visited = {self.pos.tup: True}

    # simulates pull towards attached point
    def move_to(self, point):
        dx, dy = point.x - self.pos.x, point.y - self.pos.y
        if abs(dx) > 1 or (abs(dx) == 1 and abs(dy) > 1):
            self.pos.x += dx / abs(dx)
        if abs(dy) > 1 or (abs(dy) == 1 and abs(dx) > 1):
            self.pos.y += dy / abs(dy)

        self.visited[self.pos.tup] = True


def simulate(motions, knot_count=2):
    if knot_count < 2:
        raise Exception("knot_count must be >1 (at least a head & tail)")

    knots = [Knot(0, 0) for _ in range(knot_count)]

    for direction, velocity in motions:
        for _ in range(velocity):
            knots[0].pos.move_dir(direction)
            target = knots[0].pos
            for knot in knots[1:]:
                knot.move_to(target)
                target = knot.pos

    return len(knots[-1].visited.keys())


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    with open(path, "r") as fp:
        motions = [line.split(' ') for line in fp]

    puzzle_input = [(d, int(v)) for d, v in motions]

    print("2 knots: ", simulate(puzzle_input))  # 6269
    print("10 knots:", simulate(puzzle_input, 10))  # 2557


if __name__ == "__main__":
    main()
