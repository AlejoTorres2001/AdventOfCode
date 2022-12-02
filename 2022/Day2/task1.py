op_map = {'A':'R','B':'P','C':'S'}
you_map = {'X':'R','Y':'P','Z':'S'}

def calculate_points(you,op):
    if you_map[you] == op_map[op]:
      return 3
    if you_map[you] == 'R' and op_map[op] == 'P' or you_map[you] == 'P' and op_map[op] == 'S' or you_map[you] == 'S' and op_map[op] == 'R':
      return 6
    return 0

with open()