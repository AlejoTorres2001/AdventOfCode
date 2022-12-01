with open("2Puzzle/commands.txt", "r") as file:
    commands = file.readlines()
    horizontal_pos = 0
    depth = 0
    aim = 0
    for cmd in commands:
        if "down" in cmd:
            aim += int(cmd.split(" ")[1])
        if "up" in cmd:
            aim -= int(cmd.split(" ")[1])
        if "forward" in cmd:
            horizontal_pos += int(cmd.split(" ")[1])
            depth += aim*int(cmd.split(" ")[1])
    print(f"horizontal position: {horizontal_pos}. depth: {depth}.aim: {aim}")
    print(f"total:{horizontal_pos*depth}")
