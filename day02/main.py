import sys


def get_path():
    try:
        return sys.argv[1]
    except IndexError:
        return 'input.txt'


def read_input(path):
    lines = []

    with open(path, "r") as fp:
        for line in fp:
            lines.append(line.strip())

    return lines


def main():
    path = get_path()
    input = read_input(path)

    # do stuff with input
    result = input

    print(result)


if __name__ == "__main__":
    main()
