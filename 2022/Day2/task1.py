op_map = {'A': 'R', 'B': 'P', 'C': 'S'}
you_map = {'X': 'R', 'Y': 'P', 'Z': 'S'}


def task1(you, op):
    return calculate_points(you_map[you], op_map[op])


def calculate_points(you_move, op_move):
    score_offset = 1 if you_move == 'R' else 2 if you_move == 'P' else 3 if you_move == 'S' else 0
    if you_move == op_move:
        return 3 + score_offset
    if you_move == 'R' and op_move == 'S' or you_move == 'P' and op_move == 'R' or you_move == 'S' and op_move == 'P':
        return 6 + score_offset
    return 0 + score_offset


def get_plays(task_cb):
    scores = []
    with open('./data.txt', 'r') as input:
        data = input.read().splitlines()
        for line in data:
            op, you = line.split(' ')
            scores.append(task_cb(you, op))
    return scores


if __name__ == '__main__':
    print(sum(get_plays(task1)))
