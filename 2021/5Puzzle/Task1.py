with (open("5Puzzle/input.txt","r"))as file:
    data = file.readlines()
    Lines=[]
    for lines in data:
        start = lines.split(" -> ")[0].strip("\n").split(",")
        end = lines.split(" -> ")[1].strip("\n").split(",")
        start_point= (start[0],start[1])
        end_point = (end[0],end[1])
        if(start_point[0] == end_point[0] or start_point[1] == end_point[1]):
            Lines.append([start_point,end_point])
            
    grid = [['.']*1000 for i in range(1000)]
    
    for line in Lines:
        start = line[0]
        end = line[1]
        if (start[0] == end[0]):
            beginning = min(int(start[1]),int(end[1]))
            end = max(int(start[1]),int(end[1]))
            for j in range(beginning,end+1):
                if(grid[int(start[0])][j] == '.'):
                    grid[int(start[0])][j] = 1
                else:
                    grid[int(start[0])][j]+=1
        else:
            beginning = min(int(start[0]),int(end[0]))
            end = max(int(start[0]),int(end[0]))
            for i in range(beginning,end+1):
                if(grid[i][int(start[1])] =='.'):
                    grid[i][int(start[1])] = 1
                else:
                    grid[i][int(start[1])]+=1
    counter=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] != '.' and grid[i][j]>=2):
                counter+=1
    print(counter)
            


    
    