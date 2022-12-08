# Day 8

## Part 1

 This problem is all about indexes and how to correctly use them inside a matrix. Here it might be helpful to start with the sample input data and if needed to draw the matrix on paper.

 we start by parsing the data and constructing the matrix out of it,
 
 ```python
 with open('./data.txt', 'r') as input:
    data = [line.removesuffix('\n') for line in input.readlines()]
```
Thanks to python's list comprehension, we get this powerful one-liner 

```python
grid = [[int(number) for number in line] for line in data]
```
In this part we need to check if a tree is visible in any direction, considering UP DOWN LEFT, and RIGHT only.

we need to think of the matrix as a grid where we can move row-wise or column-wise as we fit,
once you've built that thinking model in your head, you can start to write the code.

we are going to use helper functions for each direction

Because we only need to check whether there is a tree in the way or not, we can stop the loop as soon as we find a tree, and return False, otherwise, we return True.

in this case, we are moving row-wise to the left edge of the grid
```python
def check_left(x_pos, y_pos):
    for i in range(y_pos-1, -1, -1):
        if grid[x_pos][i] >= grid[x_pos][y_pos]:
            return False
    return True
```
in this case, we are moving row-wise to the right edge of the grid

Notice how the range is defined, we start from the current position and go to the end of the grid, which is the length of the first row, which is the length of the grid itself.
```python
def check_right(x_pos, y_pos):
    for i in range(y_pos+1, len(grid[0])):
        if grid[x_pos][i] >= grid[x_pos][y_pos]:
            return False
    return True
```
Now we move column-wise to the upper edge of the grid

```python
def check_up(x_pos, y_pos):
    for i in range(x_pos-1, -1, -1):
        if grid[i][y_pos] >= grid[x_pos][y_pos]:
            return False
    return True
```

Look at how the range changes from each pair of helper functions

```python
def check_down(x_pos, y_pos):
    for i in range(x_pos+1, len(grid)):
        if grid[i][y_pos] >= grid[x_pos][y_pos]:
            return False
    return True
```

with this in place we need to iterate over the grid and check for each position if the tree is visible from any direction, if it is, we increment the counter.

```python
visible_trees = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):

        if check_left(i, j) or check_right(i, j) or check_up(i, j) or check_down(i, j):
            visible_trees += 1

print(visible_trees)
```

## Part 2

We only need to change our helper functions a bit, now we care about the scenic score of each tree, this is just how many trees can you see in each direction from that particular location in the grid 
  
instead of returning  a flag we are going to keep a record of how many trees fit the condition and return that number
```python

  def get_left_score(x_pos, y_pos):
    views = 0
    for i in range(y_pos-1, -1, -1):
        views += 1
        if grid[x_pos][i] >= grid[x_pos][y_pos]:
            break
    return views


def get_right_score(x_pos, y_pos):
    views = 0
    for i in range(y_pos+1, len(grid[0])):
        views += 1
        if grid[x_pos][i] >= grid[x_pos][y_pos]:
            break
    return views


def get_up_score(x_pos, y_pos):
    views = 0
    for i in range(x_pos-1, -1, -1):
        views += 1
        if grid[i][y_pos] >= grid[x_pos][y_pos]:
            break
    return views


def get_down_score(x_pos, y_pos):
    views = 0
    for i in range(x_pos+1, len(grid)):
        views += 1
        if grid[i][y_pos] >= grid[x_pos][y_pos]:
            break
    return views
```

We need the max number  of them  all

```python
scenic_scores = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        left_score = get_left_score(i, j)
        right_score = get_right_score(i, j)
        up_score = get_up_score(i, j)
        bottom_score = get_down_score(i, j)

        scenic_scores.append(left_score * right_score *
                             up_score * bottom_score)

print(max(scenic_scores))
```