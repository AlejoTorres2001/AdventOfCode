import numpy as np

with open("9Puzzle/input.txt") as file:
    data = file.read().splitlines()
    grid = [[int(i) for i in line] for line in data]



low_points = []
basin_id = 1
basins_grid = np.zeros((len(grid), len(grid[0])), dtype=int)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        is_low = True
        for directions in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            row = i + directions[0]
            col = j + directions[1]

            if not ((0 <= row and row < len(grid)) and (0 <= col and col < len(grid[0]))):
                continue

            if grid[row][col] <= grid[i][j]:
                is_low = False
                break

        if is_low:
            low_points.append((i, j))

# DFS
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


sizes = [0] * basin_id

for x in basins_grid.flatten():
    sizes[x] += 1
sizes = sizes[1:]

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])