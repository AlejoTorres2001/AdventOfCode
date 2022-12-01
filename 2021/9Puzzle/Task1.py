with open("9Puzzle/input.txt", "r") as file:
    data = file.read().splitlines()
    grid = [[int(i) for i in line] for line in data]
risk_levels = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        is_low_point = True

        for direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            row = i+direction[0]
            col = j+direction[1]
            if not ((0 <= row and row < len(grid)) and (0 <= col and col < len(grid[0]))):
                continue

            if grid[row][col] <= grid[i][j]:
                is_low = False
                break
        if is_low_point:
            risk_levels.append(grid[i][j]+1)
print(sum(risk_levels))
