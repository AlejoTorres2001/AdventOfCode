def check_flag(partial_buffer,index):
    if len(partial_buffer) < 14 :
      return 
    if(len(set(partial_buffer)) == len(partial_buffer)):
      print(index + 1)
      return True

with open('./data.txt','r') as input:
  data:list[str] = [line.removesuffix('\n') for line in input.readlines()]
  
  for buffer in data:
    partial_buffer = ""
    for index,char in enumerate(buffer):
      partial_buffer = partial_buffer[1:] + "".join(buffer[index]) if len(partial_buffer) % 14 == 0 else partial_buffer + "".join(buffer[index])
      stop = check_flag(partial_buffer,index)
      if stop:
        break