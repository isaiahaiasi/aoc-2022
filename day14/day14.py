import sys

EMPTY = '.'
ROCK = '#'
SAND = 'o'


def sign(x):
    return 0 if x == 0 else x//abs(x)


class Grid:
    def __init__(self, w, h, default=EMPTY):
        self.w = w
        self.h = h
        self.grid = [[default]*w for _ in range(h)]

    def add(self, pos, item):
        x, y = pos
        self.grid[y][x] = item

    def get(self, pos):
        x, y = pos
        return self.grid[y][x]

    def debug_view(self):
        out = []
        for i in self.grid[:100]:
            out += [''.join(map(str, i[:100]))]
        return '\n'.join(out)


def drop_sand(grid, entry_pos=(500, 0)):
    cx, cy = entry_pos
    try:
        while True:
            if grid.get((cx, cy + 1)) == EMPTY:
                cy += 1
            elif grid.get((cx - 1, cy + 1)) == EMPTY:
                cx, cy = cx - 1, cy + 1
            elif grid.get((cx + 1, cy + 1)) == EMPTY:
                cx, cy = cx + 1, cy + 1
            else:
                grid.add((cx, cy), SAND)
                return True
    except IndexError:
        # keep trying until you run off the map, lol
        return False


def get_rocks(data):
    rocks = []
    for line in data:
        rocks.append(line[0])
        for i in range(1, len(line)):
            xa, ya = line[i-1]
            xb, yb = line[i]
            xd, yd = xb - xa, yb - ya
            for j in range(abs(xd) + abs(yd)):
                rocks.append([xa + (sign(xd) * (j + 1)),
                             ya + (sign(yd) * (j + 1))])
    return rocks


def test_cardinal(rockline):
    px, py = rockline[0]
    for x, y in rockline[1:]:
        if x != px and y != py:
            return False
        px, py = x, y
    return True


def load_input(path):
    with open(path, "r") as fp:
        rocks = []
        for line in fp.readlines():
            points = [[int(x) for x in v.split(',')]
                      for v in line.strip().split(' -> ')]
            rocks += [points]
        return rocks


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day14/test-input.txt'
    data = load_input(path)

    grid = Grid(999, 999)
    # print(get_rocks(data))

    for coords in get_rocks(data):
        grid.add(coords, ROCK)

    sand_count = 0
    while True:
        if drop_sand(grid):
            sand_count += 1
        else:
            break

    print(grid.debug_view(), sand_count)


if __name__ == "__main__":
    main()
