# Day 9
**The first graph problem!**

we are instructed to find the low points out of a grid (our input)

```python

with open("9Puzzle/input.txt", "r") as file:
    data = file.read().splitlines()
    grid = [[int(i) for i in line] for line in data]

```
we are going to have a low point if every adjacent point is bigger than that point.

you can think of this grid as a map where numbers mean the hight of the terrain, so low surrounded by high numbers would be something like a valley or basin .

to cover all 4 possible neighbors out of a pint we are going to use this trick
```python

for i in range(len(grid)):
    for j in range(len(grid[0])):
        is_low_point = True

        for direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            row = i+direction[0]
            col = j+direction[1]

```

but now we need to make sure we don't get an index error by trying to compare a position outside the bounds of our grid, this will happen when we are at the corners or sides of our grid
```python

if not ((0 <= row and row < len(grid)) and (0 <= col and col < len(grid[0]))):
                continue


```
we are going to start by assuming this point is a low point 
if it is, we are going to append its risk´s level (it´s value +1)
```python
if grid[row][col] <= grid[i][j]:
                is_low = False
                break
        if is_low_point:
            risk_levels.append(grid[i][j]+1)
```
the answer to this part is the sum of all risk levels 
```python
print(sum(risk_levels))
```


## Second part!
**Now we care about the basins formed out of a low point**

so we need and algorithm that will find all the basins in our grid,I opted for using depth-first search 

*things to keep in mind*

* *we don't have to re-visit points*

* *9 will be our boundaries to separate each basin*

instead of caring about the risk level, we are going to store the cords of the low_points 

```python
if is_low:
        low_points.append((i, j))
```

we are going to implement DFS by using a stack of points that we have to visit and a set of visited points to keep track of which ones we already visited
```python
for i, j in low_points:
    stack = [(i, j)]
    visited = set()
```

we are going to use the same trick as before to find all the adjacent points
our conditions to skip that node will be if it is a 9 or if it is out of the boundaries 
```python
 for directions in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            row = i + directions[0]
            col = j + directions[1]

            if not ((0 <= row and row < len(grid)) and (0 <= col and col < len(grid[0]))):
                continue

            if grid[row][col] == 9:
                continue

            stack.append((row, col))
```

In addition to that, we are going to have a basins_grid where we are going to mark each point with the "basin_id" so we can later retrieve the dimensions of that basin
```python
for i, j in low_points:
    stack = [(i, j)]
    visited = set()
    while len(stack) > 0:
        i, j = stack.pop()

        if (i, j) in visited:
            continue
        visited.add((i, j))

        basins_grid[i, j] = basin_id

        for directions in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            row = i + directions[0]
            col = j + directions[1]

            if not ((0 <= row and row < len(grid)) and (0 <= col and col < len(grid[0]))):
                continue

            if grid[row][col] == 9:
                continue

            stack.append((row, col))

    basin_id += 1
```

finally we make a list out of our basin_grid and retrieve the amount of point each basins contains 
we just need to multiply the three biggest basins to get our answear

```python
sizes = [0] * basin_id

for x in basins_grid.flatten():
    sizes[x] += 1
sizes = sizes[1:]

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
```
