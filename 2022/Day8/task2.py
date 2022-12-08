with open('./data.txt', 'r') as input:
    data = [line.removesuffix('\n') for line in input.readlines()]


grid = [[int(number) for number in line] for line in data]


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
