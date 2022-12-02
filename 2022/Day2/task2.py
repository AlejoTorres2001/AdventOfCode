from task1 import get_plays, op_map, calculate_points

lose_map = {'P': 'R', 'R': 'S', 'S': 'P'}
win_map = {'R': 'P', 'P': 'S', 'S': 'R'}


def calculate_play(op_play, play_should_end):
    if play_should_end == 'X':
        return lose_map[op_play]
    if play_should_end == 'Z':
        return win_map[op_play]
    return op_play


def task2(play_should_end, op):
    op_play = op_map[op]
    my_play = calculate_play(op_play, play_should_end)
    return calculate_points(my_play, op_play)


if __name__ == '__main__':
    print(sum(get_plays(task2)))
