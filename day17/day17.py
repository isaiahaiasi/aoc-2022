import sys

'''
ROCKS:
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

Each rock appears so that its left edge is two units away from the left wall
and its bottom edge is three units above the highest rock in the room
(or the floor, if there isn't one).

PART 2: hilariously large number of rocks. Simulating all not feasible.
To avoid that, is it possible to find a pattern where we know it will just keep repeating?
'''


def tuple_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


# define rocks as a set of relative points
ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],   # horizontal line
    [(0, 1), (1, 0), (1, 2), (2, 1)],   # cross (don't need middle point)
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # backward L
    [(0, 0), (0, 1), (0, 2), (0, 3)],   # vertical line
    [(0, 0), (1, 0), (0, 1), (1, 1)],   # square
]

CAVE_WIDTH = 7


class Solver:
    def __init__(self, jets: list[bool]):
        self.jets = jets  # True = right; False = left
        self.jet_index = 0
        self.cave = []

    @property
    def highest(self):
        return len(self.cave)

    def next_jet(self):
        jet = self.jets[self.jet_index]
        self.jet_index = (self.jet_index + 1) % len(self.jets)
        return 1 if jet else -1

    def check_collision(self, x, y):
        return (x < 0
                or x >= CAVE_WIDTH
                or y < 0
                or (y < self.highest and self.cave[y][x]))

    def apply_impulse(self, origin, impulse, rock) -> tuple[int, int]:
        target_origin = tuple_add(origin, impulse)
        for point in rock:
            x, y = tuple_add(point, target_origin)
            if self.check_collision(x, y):
                return origin
        return target_origin

    # gets position of where the dropped rock lands
    def drop_rock(self, rock) -> tuple[int, int]:
        origin = (2, self.highest + 3)
        while True:
            jet = self.next_jet()
            origin = self.apply_impulse(origin, (jet, 0), rock)

            next_origin = self.apply_impulse(origin, (0, -1), rock)
            if next_origin == origin:
                break
            else:
                origin = next_origin
        return origin

    def set_rock(self, rock, origin):
        for point in rock:
            x, y = tuple_add(point, origin)
            while y >= self.highest:
                self.cave.append([False]*CAVE_WIDTH)
            self.cave[y][x] = True

    def find_cycle(self):
        # TODO
        pass

    def simulate(self, times=2022):
        for i in range(times):
            if i % 100_000 == 0:
                print(i)
            rock = ROCKS[i % len(ROCKS)]
            fallen_rock_pos = self.drop_rock(rock)
            self.set_rock(rock, fallen_rock_pos)
        print(self.print_debug())
        return self.highest

    def print_debug(self, start=0, end=None):
        end = end or self.highest
        out = []
        for i, row in enumerate(self.cave[start:end]):
            r = [str(i + start), '\t\t']
            for col in row:
                r.append('█' if col else '_')
            out.append(''.join(r))
        out.reverse()
        return '\n'.join(out)


def load_input(path):
    with open(path, "r") as fp:
        return [True if j == '>' else False for j in fp.read()]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day17/test-input.txt'
    jets = load_input(path)

    result = Solver(jets).simulate(100)
    # result = Solver(jets).simulate(1_000_000_000_000)

    print(result)


if __name__ == "__main__":
    main()
