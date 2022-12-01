with open("10Puzzle/input.txt", "r") as file :
    data = file.read().strip()
    lines = data.split("\n")
pairs = ["()", "[]", "<>", "{}"]
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
total=0

def is_correct(line:str)->int:
    stack = []
    for char in line:
        valid = False
        for p in pairs:
            if char == p[0]:
                stack.append(char)
                valid = True
            elif char == p[1]:
                if stack[-1] == p[0]:
                    stack.pop()
                    valid = True

        if not valid:
            return scores[char]

    return 0

for line in lines:
    total+=is_correct(line)
print(total)