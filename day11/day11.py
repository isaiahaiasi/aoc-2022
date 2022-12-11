import sys
import re
from math import prod

monkeys = []
shared_multiple = 1


class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspect_count = 0
        global shared_multiple

        # ought to be Least Common Multiple, but meh
        shared_multiple *= test['mod']

    def operate(self, item):
        op, t = self.operation
        # need to handle ONE exceptional line in input data: "old * old"
        term_2 = item if t == 'old' else int(t)
        match op:
            case "+": return item + term_2
            case "*": return item * term_2

    def turn(self, part):
        for item in self.items:
            # print(f"Inspects item with a worry level of {item}")
            # inspect each item
            item = self.operate(item)

            # print(f"Worry level increased to {item}")
            item = item // 3 if part == 1 else item % shared_multiple

            # print(f"Worry reduced to {item}")

            toss_target = self.test[item % self.test['mod'] == 0]
            # print(f"Tossing to Monkey {toss_target}")
            monkeys[toss_target].items.append(item)
            self.inspect_count += 1
        self.items = []


def solve(rounds, part=1):
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            # print(f'Monkey {i}:')
            monkey.turn(part)
    inspections = [m.inspect_count for m in monkeys]
    inspections.sort(reverse=True)
    return prod(inspections[:2])


def load_input(path):
    with open(path, "r") as fp:
        monkey_data = [m.split('\n') for m in fp.read().split('\n\n')]
        for monkey in monkey_data:
            items = [int(n) for n in re.findall('\d{1,}', monkey[1])]
            operation = monkey[2].split('old ')[1].split(' ')
            test = {
                'mod': int(monkey[3].split('divisible by ')[1]),
                True: int(monkey[4].split('monkey ')[1]),
                False: int(monkey[5].split('monkey ')[1])
            }
            monkeys.append(Monkey(items, operation, test))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './day11/test-input.txt'

    load_input(path)

    # PART A: (commented out bc lots of mutations I'm too lazy to clean up)
    # result = solve(20, 1) # 66802

    # PART B:
    result = solve(10000, 2)  # 21800916620

    print(result)


if __name__ == "__main__":
    main()
