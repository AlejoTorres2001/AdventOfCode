def get_stacks(data):
  stacks_row =''
  for index,row in enumerate(data):
    if row == '\n':
      stacks_row = data[index-1]
  return [stack for stack in stacks_row.removesuffix('\n').split(' ') if stack != '']

def parse_stacks(stacks,stacks_data):
  crates_stacks = {}
  offset=1
  for stack in stacks:
    for line in stacks_data:
      if line[offset] == ' ' or line[offset] == '\n':
        continue
      crates_stacks[stack] = crates_stacks.get(stack,[]) + [line[offset]]
    offset += 4
  return crates_stacks

def parse_indications(indications_data):
  parsed_indications = []
  for indication in indications_data:
    if indication != '\n':
      data = indication.removesuffix('\n').split(' ')
      parsed_indications.append((int(data[1]),int(data[3]),int(data[5])))
  return parsed_indications


def move_create(create_stacks,indication):
  stack_from:list = create_stacks[str(indication[1])]
  stack_to:list = create_stacks[str(indication[2])]
  creates_qty = indication[0]
  for _ in range(creates_qty):
    stack_to.insert(0,stack_from.pop(0))

def get_first_crates(create_stacks):
  first_crates = []
  for stack in create_stacks.values():
    first_crates.append(stack[0])
  return first_crates
if __name__ == '__main__':
  with open('./data.txt','r') as input:
    data = input.readlines()
    stacks = get_stacks(data)
    stacks_data = data[:data.index('\n')-1]
    crate_stacks = parse_stacks(stacks,stacks_data)
    indications_data=data[data.index('\n')+1:]
    indications = parse_indications(indications_data)
    for indication in indications:
      move_create(crate_stacks,indication)
    print("".join(get_first_crates(crate_stacks)))