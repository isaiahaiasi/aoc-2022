import sys
from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solver:
    def __init__(self, grid):
        self.grid = grid
        self.end = self.get_pos('E')
        self.start = self.current = self.get_pos('S')
        self.grid[self.start[1]][self.start[0]] = ord('a')
        self.grid[self.end[1]][self.end[0]] = ord('z')
        self.h = len(grid)
        self.w = len(grid[0])

    def get_pos(self, ltr):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == ord(ltr):
                    return (x, y)

    def in_range(self, x, y):
        return x >= 0 and y >= 0 and y < self.h and x < self.w

    def get_neighbors(self, x, y):
        adjacent_coords = []
        for dx, dy in DIRS:
            if self.in_range(x + dx, y + dy):
                if self.grid[y + dy][x + dx] - self.grid[y][x] <= 1:
                    adjacent_coords.append((x + dx, y + dy))
        return adjacent_coords

    def bfs_1(self):
        queue = deque()
        visited = {}
        visited[self.start] = 0
        queue.append(self.start)

        while queue:
            r = queue.popleft()
            for n in self.get_neighbors(*r):
                if n not in visited or visited[n] > visited[r] + 1:
                    visited[n] = visited[r] + 1
                    queue.append(n)
        return visited[self.end]

    def get_neighbors_reversed(self, x, y):
        adjacent_coords = []
        for dx, dy in DIRS:
            if self.in_range(x + dx, y + dy):
                if self.grid[y][x] - self.grid[y + dy][x + dx] <= 1:
                    adjacent_coords.append((x + dx, y + dy))
        return adjacent_coords

    # searching from end, trying to find the first 'a'
    def bfs_2(self):
        queue = deque()
        visited = {self.end: 0}
        queue.append(self.end)

        while queue:
            r = queue.popleft()
            for (x, y) in self.get_neighbors_reversed(*r):
                if (x, y) not in visited or visited[(x, y)] > visited[r] + 1:
                    visited[(x, y)] = visited[r] + 1
                    queue.append((x, y))
                    if self.grid[y][x] == ord('a'):
                        return visited[(x, y)]

    def print_debug(self, visited):
        out = [[' ']*self.w + ['\n'] for _ in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                if (x, y) in visited:
                    out[y][x] = chr(self.grid[y][x])
        print(''.join([''.join(line) for line in out]))


def load_input(path):
    with open(path, "r") as fp:
        return [[ord(c) for c in list(line.strip())] for line in fp]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day12/input.txt'
    grid = load_input(path)

    solver = Solver(grid)

    print(solver.bfs_1())
    print(solver.bfs_2())


if __name__ == "__main__":
    main()
