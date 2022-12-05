import sys
import re


class CargoManager:
    def __init__(self, stacks):
        self.stacks = stacks

    def move_crates_individual(self, instructions):
        for [count, start, end] in instructions:
            for _ in range(count):
                item = self.stacks[start].pop()
                self.stacks[end].append(item)

    def move_crates_multiple(self, instructions):
        for [count, start, end] in instructions:
            self.stacks[end] += self.stacks[start][-count:]
            self.stacks[start] = self.stacks[start][:-count]


def parse_drawing(drawing):
    drawing = drawing.split('\n')
    col_count = len(drawing[0])//4 + 1
    stacks = [[] for _ in range(col_count)]
    for line in drawing:
        for col, i in enumerate(range(col_count)):
            line_index = col + 1 + i * 3
            char = line[line_index]
            if char.isupper():
                stacks[col].insert(0, char)
    return stacks


def load_input(path):
    instructions = []
    with open(path, "r") as fp:
        input = fp.read()
        [drawing, raw_instructions] = input.split('\n\n')
        for line in raw_instructions.split('\n'):
            [cnt, start, end] = [int(n) for n in re.findall('\d{1,}', line)]
            instructions.append([cnt, start - 1, end - 1])
        return [parse_drawing(drawing), instructions]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    [stacks, instructions] = load_input(path)
    cargoManager = CargoManager(stacks)
    cargoManager.move_crates_multiple(instructions)
    print('result:', ''.join([n[-1] for n in cargoManager.stacks]))


if __name__ == "__main__":
    main()
