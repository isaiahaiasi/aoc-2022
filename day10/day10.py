import sys


def get_register_history(input):
    cycles = [1]
    x = 1
    for op in input:
        cycles.append(x)
        if len(op) == 1:
            continue
        x += int(op[1])
        cycles.append(x)
    return cycles


def part_1(input):
    hist = get_register_history(input)
    return sum([(hist[i - 1] * i) for i in range(20, 241, 40)])


def part_2(input):
    reg_history = get_register_history(input)
    output = []
    for i, reg in enumerate(reg_history[:-1]):
        pixels = [n % 40 for n in range(reg-1, reg+2)]
        pixel = '#' if i % 40 in pixels else '_'
        output.append(pixel)
        if i % 40 + 1 == 40:
            output.append('\n')
    return ''.join(output)  # avoids expensive string concatenation


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day10/test-input.txt'
    with open(path, "r") as fp:
        input = [line.strip().split(' ') for line in fp]

    print(f"PART 1:\n{part_1(input)}")
    print(f"PART 2:\n{part_2(input)}", end='')


if __name__ == "__main__":
    main()
