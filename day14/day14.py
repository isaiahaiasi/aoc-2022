import sys
from itertools import chain

EMPTY = '.'
ROCK = '#'
SAND = 'o'


def sign(x):
    return 0 if x == 0 else x//abs(x)


class Cave:
    def __init__(self, rocks, floor=None):
        self.floor = floor
        self.grid = {}
        for coords in rocks:
            self.add(coords, ROCK)

    def add(self, pos, item):
        x, y = pos
        self.grid[(x, y)] = item

    def get(self, pos):
        x, y = pos
        if self.floor and y >= self.floor:
            return ROCK
        return self.grid.get((x, y), EMPTY)


def drop_sand(grid, giveup_height=None, entry_pos=(500, 0)):
    cx, cy = entry_pos
    while True:
        if giveup_height and cy > giveup_height:
            return False
        elif grid.get((cx, cy + 1)) == EMPTY:
            cy += 1
        elif grid.get((cx - 1, cy + 1)) == EMPTY:
            cx, cy = cx - 1, cy + 1
        elif grid.get((cx + 1, cy + 1)) == EMPTY:
            cx, cy = cx + 1, cy + 1
        else:
            grid.add((cx, cy), SAND)
            return (cx, cy) != entry_pos


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


def get_lowest(rocks):
    return max([y for x, y in list(chain(rocks))])


def part_1(rocks):
    grid = Cave(rocks)
    sand_count = 0
    lowest_rock_height = get_lowest(rocks)
    while True:
        if drop_sand(grid, lowest_rock_height):
            sand_count += 1
        else:
            break
    return sand_count


def part_2(rocks):
    grid = Cave(rocks, get_lowest(rocks) + 2)

    sand_count = 0
    while True:
        sand_count += 1
        if not drop_sand(grid):
            break
    return sand_count


def load_input(path):
    with open(path, "r") as fp:
        rocks = []
        for line in fp.readlines():
            points = [[int(x) for x in v.split(',')]
                      for v in line.strip().split(' -> ')]
            rocks += [points]
        return rocks


path = sys.argv[1] if len(sys.argv) > 1 else './day14/test-input.txt'
data = load_input(path)

rock_data = get_rocks(data)

print("PART A:", part_1(rock_data))
print("PART B:", part_2(rock_data))
