import itertools
with open("8Puzzle\input.txt") as file:
    displays = [lines.strip("\n") for lines in file.readlines()]
    
digits_key = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]

digits = tuple(sorted(digits_key))

total = 0

for dp in displays:
    signals,outputs = dp.split("|")
    signals = signals.strip().split(" ")
    outputs = outputs.strip().split(" ")
    
    for sigma in itertools.permutations("abcdefg"):
        key = {}
        for char in "abcdefg":
            key[char] = sigma["abcdefg".index(char)]

        possible_combination = []
        for signal in signals:
            decoded = ""
            for char in signal:
                decoded += key[char]
            decoded = "".join(sorted(decoded))
            possible_combination.append(decoded)

        possible_combination.sort()

        if tuple(possible_combination) == digits:
            
            decoded_outputs = []
            for output in outputs:
                decoded_output = ""
                for char in output:
                    decoded_output += key[char]
                decoded_output = "".join(sorted(decoded_output))
                decoded_outputs.append(digits_key.index(decoded_output))

            total += int("".join([str(i) for i in decoded_outputs]))

            break
print(total)

