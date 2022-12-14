import sys
from itertools import chain


def sign(x): return 0 if x == 0 else x//abs(x)


class Cave:
    def __init__(self, rocks, has_floor=False):
        self.w, self.h = 1000, 1000
        self.obstacles = [[False]*self.w for _ in range(self.h)]
        self.lowest = max([y for x, y in list(chain(rocks))])
        self.has_floor = has_floor

        for x, y in rocks:
            self.add_obstacle(x, y)
        if has_floor:
            for i in range(self.w):
                self.add_obstacle(i, self.lowest + 2)

    def add_obstacle(self, x, y):
        self.obstacles[y][x] = True

    def has_obstacle(self, x, y):
        return self.obstacles[y][x]

    def drop_sand(self, entry_x=500, entry_y=0):
        cx, cy = entry_x, entry_y
        while True:
            if (self.has_obstacle(entry_x, entry_y)
                    or cy > self.lowest and not self.has_floor):
                return False
            elif not self.has_obstacle(cx, cy + 1):
                cy += 1
            elif not self.has_obstacle(cx - 1, cy + 1):
                cx, cy = cx - 1, cy + 1
            elif not self.has_obstacle(cx + 1, cy + 1):
                cx, cy = cx + 1, cy + 1
            else:
                self.add_obstacle(cx, cy)
                cx, cy = entry_x, entry_y
                yield True


def get_rocks(data):
    rocks = []
    for line in data:
        rocks.append(line[0])
        for i in range(1, len(line)):
            xa, ya = line[i-1]
            xb, yb = line[i]
            xd, yd = xb - xa, yb - ya
            for j in range(abs(xd) + abs(yd)):
                x_incr, y_incr = sign(xd) * (j + 1), sign(yd) * (j + 1)
                rocks.append((xa + x_incr, ya + y_incr))
    return rocks


def load_input(path):
    with open(path, "r") as fp:
        rocks = []
        for line in fp.readlines():
            rocks.append([tuple([int(x) for x in v.split(',')])
                          for v in line.strip().split(' -> ')])
        return rocks


path = sys.argv[1] if len(sys.argv) > 1 else './day14/test-input.txt'
rock_data = get_rocks(load_input(path))
print("PART A:", sum(Cave(rock_data).drop_sand()))  # 1072
print("PART B:", sum(Cave(rock_data, has_floor=True).drop_sand()))  # 24_659
