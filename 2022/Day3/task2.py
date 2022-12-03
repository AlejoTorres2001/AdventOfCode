from task1 import item_types_map


def three_rucksacks_intersection(rucksack1: str, rucksack2: str, rucksack3: str):
    intersection = []
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            intersection.append(item)
    return set(intersection)


with open('./data.txt', 'r') as input:
    total_priority = 0
    data = [line.removesuffix('\n') for line in input.readlines()]
    for i in range(0, len(data), 3):
        intersection = three_rucksacks_intersection(
            data[i], data[i+1], data[i+2])
        for value in intersection:
            total_priority += item_types_map[value]

if __name__ == '__main__':
    print(total_priority)
