# [[(),()], [(),()]]
def get_pairs():
    with open('./data.txt', 'r') as input:
        data = [line.removesuffix('\n') for line in input.readlines()]
    parsed_data = []
    for line in data:
        pair = line.split(',')
        parsed_data.append(
            [
                (int(pair[0].split('-')[0]), int(pair[0].split('-')[1])),
                (int(pair[1].split('-')[0]), int(pair[1].split('-')[1]))
            ]
        )
    return parsed_data


def task1():
    overlapped_pairs = 0
    for pairs in get_pairs():
        min_pair = min(pairs, key=lambda x: x[0])
        if min_pair[1] >= max(pairs, key=lambda x: x[0])[1]:
            overlapped_pairs += 1
    return overlapped_pairs


if __name__ == '__main__':
    print(task1())
