import sys
with open("7Puzzle\input.txt", "r") as file:
    data = file.read().strip("\n")
    positions = [int(x) for x in data.split(",")]
    min_fuel = sys.maxsize
    for i in range(len(positions)):
        fuel=0
        for j in range(len(positions)):
            part_fuel=0
            distance = abs(positions[i] - positions[j])
            for k in range(1,distance+1):
                part_fuel+=k
            fuel += part_fuel
        if fuel < min_fuel:
            position = positions[i]
            min_fuel = fuel
print(f"min amount of fuel is {min_fuel} to get to {position}")