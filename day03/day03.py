import sys


def get_common(rucksack):
    middle = len(rucksack)//2
    first_half = rucksack[:middle]
    second_half = rucksack[middle:]

    # worse time complexity but quick lol
    for item in first_half:
        for other_item in second_half:
            if item == other_item:
                return item
    raise Exception('no shared item')


def get_badge(sacks):
    # HORRIBLE time complexity but probably quick enough...
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


def get_priority_sum(input):
    priority_sum = 0
    for rucksack in input:
        priority_sum += get_priority(get_common(rucksack))
    return priority_sum


# get groups (each 3 lines)
# find shared char between each 3
# get sum of value of each "badge"
def get_badge_sum(input):
    badge_sum = 0
    group_count = len(input) // 3
    for i in range(group_count):
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

    print(get_priority_sum(input))
    print(get_badge_sum(input))


if __name__ == "__main__":
    main()
