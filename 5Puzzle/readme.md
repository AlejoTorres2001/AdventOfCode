# Day 5
**I enjoyed this one, part 1 was kind of easy because we only care about horizontal or vertical lines, then on part 2 I had to wrapped my head around the diagonals**

First of all we need to work our way around the input data 
which in this case was in the following format
```python
591,311 -> 289,311
```
those pairs of numbers pointed out the initial and ending coordinates of a given line
I opted for making touples with each point and then making a list for each set of points so I ended up with a list of lists wich contains the initial and ending coordinates of each line 
```python
with (open("5Puzzle/input.txt","r"))as file:
    data = file.readlines()
    Lines=[]
    for lines in data:
        start = lines.split(" -> ")[0].strip("\n").split(",")
        end = lines.split(" -> ")[1].strip("\n").split(",")
        start_point= (start[0],start[1])
        end_point = (end[0],end[1])
```
in part 1 we only need vertical or horizontal lines so we have to filter them 
```python
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
 ```
Now we need a grid, looking through the inputs  I noticed that the biggest number was 998 so I played it safe and made a 1000x1000 grid
probably the best way to do this is to get the max number for x and y and build a grid around those values, but 1000x1000 worked fine 
```python
 grid = [['.']*1000 for i in range(1000)]
 ```
We have to iterate through the *Lines* taking its start and end points 
we check if happens to ve a vertical or horizontal line by looking at the values of x and y and finding matches 
```python
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
 ```
 then we have to properly address the beginning and the end coordinates so we can use them in the range function
 ```python
  beginning = min(int(start[1]),int(end[1]))
            end = max(int(start[1]),int(end[1]))
            for j in range(beginning,end+1):
                if(grid[int(start[0])][j] == '.'):
                    grid[int(start[0])][j] = 1
                else:
                    grid[int(start[0])][j]+=1
 ```
 if what it found was a '.' we change it to a 1 otherwise add +1 
 
 The same goes for vetical lines
  ```python
 else:
            beginning = min(int(start[0]),int(end[0]))
            end = max(int(start[0]),int(end[0]))
            for i in range(beginning,end+1):
                if(grid[i][int(start[1])] =='.'):
                    grid[i][int(start[1])] = 1
                else:
                    grid[i][int(start[1])]+=1
  ```
 Finally we have to iterate through the grid counting the points where 2 or more lines went through
  ```python
 counter=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] != '.' and grid[i][j]>=2):
                counter+=1
  ```
  
  ## Second Part!
  **I found it slightly tricky to understand the behavior of diagonal lines**
  
  * we can have diagonals with a positive slope (means the pint upwards)
  
  * or we can have them with negative slopes (the line points downwards)
  * 
 *We DON'T need to filter the lines at first*
 
 we are going to rearrange the end and start according to who is bigger this way we will be able to use them in the range function as seen before
 ```python
  else:
            if start[0] > end[0]:
                line = [end, start]
            for spot in range(line[1][0]-line[0][0]+1):
```

To properly tray the trajectory of the line we need to know if we are moving up or down in the grid
 ```python
for spot in range(line[1][0]-line[0][0]+1):
                vertical = spot if line[1][1] > line[0][1] else -spot
                horizontal = spot if line[1][0] > line[0][0] else -spot
                if(grid[line[0][0]+horizontal][line[0][1]+vertical] == '.'):
                    grid[line[0][0]+horizontal][line[0][1]+vertical] = 1
                else:
                    grid[line[0][0]+horizontal][line[0][1]+vertical] += 1
 ```
 The final part is the same as before, we go through the entire grid counting where 2 or more lines went through
  ```python
  counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] != '.' and grid[i][j] >= 2):
                counter += 1
    print(counter)
```
 
  
