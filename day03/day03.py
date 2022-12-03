import sys


def get_type(rucksack):
    middle = len(rucksack)//2
    sack1 = rucksack[:middle]
    sack2 = rucksack[middle:]

    # worse time complexity but quick lol
    # n^2, stop at first shared
    for item in sack1:
        for other_item in sack2:
            if item == other_item:
                return item
    raise Exception('no shared item')


def get_badge(sacks):
    # HORRIBLE time complexity but probably quick enough...
    # n^3, stop at first shared
    for item1 in sacks[0]:
        for item2 in sacks[1]:
            for item3 in sacks[2]:
                if item1 == item2 and item1 == item3:
                    return item1
    raise Exception('no shared item')


def get_priority(item: str):
    # a-z: 1-26
    # A-Z: 27-52
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def priority_sum(input):
    rucksack_sum = 0
    for rucksack in input:
        rucksack_sum += get_priority(get_type(rucksack))
    return rucksack_sum


# get groups (each 3 lines)
# find shared char between each 3
# get sum of value of each "badge"
def get_badge_sum(input):
    badge_sum = 0
    group_cnt = len(input) // 3
    for i in range(group_cnt):
        rucksacks = input[i * 3: i * 3 + 3]
        badge = get_badge(rucksacks)
        badge_sum += get_priority(badge)
    return badge_sum


def load_input(path):
    lines = []
    with open(path, "r") as fp:
        for line in fp:
            lines.append(line.strip())
    return lines


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    input = load_input(path)

    result = get_badge_sum(input)

    print(result)


if __name__ == "__main__":
    main()
