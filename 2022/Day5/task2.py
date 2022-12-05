from task1 import get_first_crates,get_stacks,parse_stacks,parse_indications

def move_create_task2(create_stacks,indication):
  stack_from:list = create_stacks[str(indication[1])]
  stack_to:list = create_stacks[str(indication[2])]
  creates_qty = indication[0]
  creates = stack_from[:creates_qty]
  for _ in range(creates_qty):
    stack_from.pop(0)
  create_stacks[str(indication[2])] = creates + stack_to

if __name__ == '__main__':
  with open('./data.txt','r') as input:
    data = input.readlines()
    stacks = get_stacks(data)
    stacks_data = data[:data.index('\n')-1]
    crate_stacks = parse_stacks(stacks,stacks_data)
    indications_data=data[data.index('\n')+1:]
    indications = parse_indications(indications_data)
    for indication in indications:
      move_create_task2(crate_stacks,indication)
    print("".join(get_first_crates(crate_stacks)))