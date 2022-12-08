with open('./data.txt', 'r') as input:
    data = [line.removesuffix('\n') for line in input.readlines()]


grid = [[int(number) for number in line] for line in data]


def check_left(x_pos, y_pos):
    for i in range(y_pos-1, -1, -1):
        if grid[x_pos][i] >= grid[x_pos][y_pos]:
            return False
    return True


def check_right(x_pos, y_pos):
    for i in range(y_pos+1, len(grid[0])):
        if grid[x_pos][i] >= grid[x_pos][y_pos]:
            return False
    return True


def check_up(x_pos, y_pos):
    for i in range(x_pos-1, -1, -1):
        if grid[i][y_pos] >= grid[x_pos][y_pos]:
            return False
    return True


def check_down(x_pos, y_pos):
    for i in range(x_pos+1, len(grid)):
        if grid[i][y_pos] >= grid[x_pos][y_pos]:
            return False
    return True


visible_trees = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):

        if check_left(i, j) or check_right(i, j) or check_up(i, j) or check_down(i, j):
            visible_trees += 1

print(visible_trees)
