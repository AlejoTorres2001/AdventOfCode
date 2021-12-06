from collections import defaultdict

with open("6Puzzle/input.txt", "r") as file:
    data = file.read().strip().split(',')
    freq = defaultdict(int)
    for d in data:
        freq[int(d)] += 1

    for _ in range(1, 257):
        new_freq = defaultdict(int)
        for key in freq:
            if key == 0:
                new_freq[6] += freq[key]
                new_freq[8] = freq[key]
            else:
                new_freq[key-1] += freq[key]
        freq = new_freq
print(freq)
total = 0
for key in freq:
    total += freq[key]
print(f"total: {total}")
