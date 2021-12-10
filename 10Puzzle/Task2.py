with open("10Puzzle/input.txt") as file:
    raw_data = file.read().strip()
    data = raw_data.split("\n")

pairs = ["()", "[]", "<>", "{}"]

bad_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
good_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def is_correct(line):
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
            return bad_scores[char]

    return 0


def complete(line):
    stack = []
    ans = 0
    for char in line:
        for p in pairs:
            if char == p[0]:
                stack.append(char)
            elif char == p[1]:
                if stack[-1] == p[0]:
                    stack.pop()

    for char in stack[::-1]:
        ans *= 5
        ans += good_scores[char]

    return ans


data = [line for line in data if is_correct(line) == 0]

scores = []
for line in data:
    scores.append(complete(line))

scores.sort()
ans = scores[len(scores) // 2]
print(ans)