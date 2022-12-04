from task1 import get_pairs


def task2():
    overlapped_pairs = 0
    for pairs in get_pairs():
        min_pair = min(pairs, key=lambda x: x[0])
        if min_pair[1] >= max(pairs, key=lambda x: x[0])[0]:
            overlapped_pairs += 1
    return overlapped_pairs


if __name__ == '__main__':
    print(task2())
