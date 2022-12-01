with open("6Puzzle/input.txt", "r") as file:
    ages = file.read()
    ages = [int(number) for number in ages if number != ',']

    for day in range(1, 81):
        for i in range(len(ages)):
            if ages[i] == 0:
                ages.append(8)
                ages[i] = 7
            if ages[i] != 0:
                ages[i] -= 1
        print(f"after {day} days: {ages}")
    total = len(ages)
    print(f"total: {total}")
