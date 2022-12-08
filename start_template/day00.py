import sys


def do_stuff(input):
    return 'todo'


def load_input(path):
    with open(path, "r") as fp:
        return [line.strip() for line in fp]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    input = load_input(path)

    result = do_stuff(input)

    print(result)


if __name__ == "__main__":
    main()
