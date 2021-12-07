import sys
with open("7Puzzle\input.txt", "r") as file:
    data = file.read().strip("\n")
    positions = [int(x) for x in data.split(",")]
    min_fuel = sys.maxsize
    for i in range(len(positions)):
        fuel=0
        for j in range(len(positions)):
            distance = abs(positions[i] - positions[j])
            fuel += distance
        if fuel < min_fuel:
            position = positions[i]
            min_fuel = fuel
print(f"min amount of fuel is {min_fuel} to get to {position}")
                
            
