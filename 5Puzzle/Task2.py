with (open("5Puzzle/input.txt", "r"))as file:
    data = file.readlines()
    Lines = []
    for lines in data:
        start = lines.split(" -> ")[0].strip("\n").split(",")
        end = lines.split(" -> ")[1].strip("\n").split(",")
        start_point = (int(start[0]), int(start[1]))
        end_point = (int(end[0]), int(end[1]))
        Lines.append([start_point, end_point])

    grid = [['.']*1000 for i in range(1000)]

    for line in Lines:
        start = line[0]
        end = line[1]
        if (start[0] == end[0]):
            beggining = min(int(start[1]), int(end[1]))
            end = max(int(start[1]), int(end[1]))
            for j in range(beggining, end+1):
                if(grid[int(start[0])][j] == '.'):
                    grid[int(start[0])][j] = 1
                else:
                    grid[int(start[0])][j] += 1
        elif(start[1] == end[1]):
            beggining = min(int(start[0]), int(end[0]))
            end = max(int(start[0]), int(end[0]))
            for i in range(beggining, end+1):
                if(grid[i][int(start[1])] == '.'):
                    grid[i][int(start[1])] = 1
                else:
                    grid[i][int(start[1])] += 1
        else:
            if start[0] > end[0]:
                line = [end, start]
            for spot in range(line[1][0]-line[0][0]+1):
                vertical = spot if line[1][1] > line[0][1] else -spot
                horizontal = spot if line[1][0] > line[0][0] else -spot
                if(grid[line[0][0]+horizontal][line[0][1]+vertical] == '.'):
                    grid[line[0][0]+horizontal][line[0][1]+vertical] = 1
                else:
                    grid[line[0][0]+horizontal][line[0][1]+vertical] += 1
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] != '.' and grid[i][j] >= 2):
                counter += 1
    print(counter)
