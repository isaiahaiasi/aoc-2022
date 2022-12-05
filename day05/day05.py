import sys
import re


def parse_drawing(drawing):
    drawing = drawing.split('\n')
    col_count = len(drawing[0])//4 + 1

    state = [[] for _ in range(col_count)]

    for line in drawing:
        for col, i in enumerate(range(col_count)):
            line_index = col + 1 + i * 3
            char = line[line_index]
            if char.isupper():
                state[col].insert(0, char)

    return state


def parse_instruction(instruction):
    res = [int(n) for n in re.findall('\d{1,}', instruction)]
    if (len(res) == 3):
        return res
    else:
        raise Exception('bad instruction input', instruction)


def handle_instructions_v2(state, instructions):
    for line in instructions:
        [_count, _from, _to] = parse_instruction(line)
        lifted = []
        for _ in range(_count):
            item = state[_from - 1].pop()
            lifted.insert(0, item)
        state[_to - 1] = state[_to - 1] + lifted


def handle_instructions_v1(state, instructions):
    for line in instructions:
        [_count, _from, _to] = parse_instruction(line)
        for _ in range(_count):
            item = state[_from - 1].pop()
            state[_to - 1].append(item)


def load_input(path):
    instructions = []
    with open(path, "r") as fp:
        input = fp.read()
        [drawing, raw_instructions] = input.split('\n\n')
        for line in raw_instructions.split('\n'):
            instructions.append(line)
        return [drawing, instructions]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

    [drawing, instructions] = load_input(path)

    state = parse_drawing(drawing)

    handle_instructions_v1(state, instructions)

    print(''.join([n[-1] for n in state]))


if __name__ == "__main__":
    main()
