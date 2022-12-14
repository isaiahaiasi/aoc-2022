import sys
from itertools import chain


def sign(x):
    return 0 if x == 0 else x//abs(x)


class Cave:
    def __init__(self, rocks, has_floor=False):
        self.obstacles = set()
        self.lowest = max([y for x, y in list(chain(rocks))])
        self.floor = self.lowest + 2 if has_floor else None
        for coords in rocks:
            self.add_obstacle(coords)

    def add_obstacle(self, pos):
        self.obstacles.add(pos)

    def has_obstacle(self, pos):
        x, y = pos
        return (x, y) in self.obstacles or (self.floor and y >= self.floor)

    def drop_sand(self, entry_pos=(500, 0)):
        cx, cy = entry_pos
        while True:
            if (self.has_obstacle(entry_pos)
                    or cy > self.lowest and not self.floor):
                return False
            elif not self.has_obstacle((cx, cy + 1)):
                cy += 1
            elif not self.has_obstacle((cx - 1, cy + 1)):
                cx, cy = cx - 1, cy + 1
            elif not self.has_obstacle((cx + 1, cy + 1)):
                cx, cy = cx + 1, cy + 1
            else:
                self.add_obstacle((cx, cy))
                cx, cy = entry_pos
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
            points = [tuple([int(x) for x in v.split(',')])
                      for v in line.strip().split(' -> ')]
            rocks += [points]
        return rocks


path = sys.argv[1] if len(sys.argv) > 1 else './day14/test-input.txt'
rock_data = get_rocks(load_input(path))
print("PART A:", sum(Cave(rock_data).drop_sand()))
print("PART B:", sum(Cave(rock_data, has_floor=True).drop_sand()))
