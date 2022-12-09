import sys


DIRECTION = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        x, y = 0, 0

        if abs(dx) > 1 or (abs(dx) == 1 and abs(dy) > 1):
            x = dx / abs(dx)
        if abs(dy) > 1 or (abs(dy) == 1 and abs(dx) > 1):
            y = dy / abs(dy)

        self.pos.x += x
        self.pos.y += y
        self.visited[self.pos.tup] = True


def simulate_single(motions):
    head = Point(0, 0)
    tail = Knot(0, 0)

    for direction, velocity in motions:
        for _ in range(velocity):
            head.move_dir(direction)
            tail.move_to(head)

    return len(tail.visited.keys())


def simulate_n(motions, n):
    head = Point(0, 0)
    knots = [Knot(0, 0) for _ in range(n)]

    for direction, velocity in motions:
        for _ in range(velocity):
            head.move_dir(direction)
            target = head
            for knot in knots:
                knot.move_to(target)
                target = knot.pos

    return len(knots[-1].visited.keys())


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    with open(path, "r") as fp:
        motions = [line.split(' ') for line in fp]

    puzzle_input = [(d, int(v)) for d, v in motions]

    print(simulate_single(puzzle_input))  # 6269
    print(simulate_n(puzzle_input, 9))  # 2557


if __name__ == "__main__":
    main()
