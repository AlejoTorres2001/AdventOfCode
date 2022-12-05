## Day 5

## Part 1

We start seeing more complex linear structures and data parsing algorithms.

The majority of the complexity is in the parsing of the data. there are two big sections to focus on
First the crate stacks which must be interpreted row-wise,and then we need to extract information from the directives, this adds an additional challenge. Let's break it down

as always we start by reading the input file

```python

  with open('./data.txt','r') as input:
    data = input.readlines()
```

our first helper function ````get_stacks````  will take the data and return a list of the stacks by targeting one row up the EOL-only line we have in the data. Its pretty important to build up skills that help you understand patterns inside data and how we can exploit them in our favor, best way is by practicing a lot!


now we know how many stacks we have to build

```` quick side note: As I'm writing this and going through the code I realized that maybe it is a bit redundant to know the sort of *id* of every stack, ni this exercise in particular, but as always I try to speed-run this challenges so not the cleanest solution out there for sure````

```python
def get_stacks(data):
  stacks_row =''
  for index,row in enumerate(data):
    if row == '\n':
      stacks_row = data[index-1]
  return [stack for stack in stacks_row.removesuffix('\n').split(' ') if stack != '']
```

Remember I told you the same input file contains two different types of data? well, now we are only interested in the upper chunk of data, the stacks.We will look for that EOL-only line and the all the data above it except the already parsed stacks identifiers.

```python 
stacks_data = data[:data.index('\n')-1]
```

Now we need to parse our stacks, we will use a dictionary to store each stack by its identifier,although we could have used a proper stack data structure, I opted for plain list objects to keep it simple.
we will iterate through the stacks and for each line in our data we will target specific idexes to extract the data we need, if you pay attention to  the input file you will notice that a space of 4 characters separates each create content from each stack except on the first case, will use this pattern to our advantage.


```python

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
```

Now we move on to the next parsing stage, the directives.

to get the part where all directives starts we will use a similar approach as before, we will look for the EOL-only line and then we will slice the data from that point on.

```python
indications_data=data[data.index('\n')+1:]
```

Now we parse those indications and generating a list of tuples with the information we need, we will use a similar approach as before, we will iterate through the data and target specific indexes to extract the data we need, the pattern we will use is that before and after each number there is a blank space 

```python
def parse_indications(indications_data):
  parsed_indications = []
  for indication in indications_data:
    if indication != '\n':
      data = indication.removesuffix('\n').split(' ')
      parsed_indications.append((int(data[1]),int(data[3]),int(data[5])))
  return parsed_indications
```

the first part is solved!!

Now to the actual ED logic, the idicantions are used to move creates between stacks, in this case we can only move one create at the time.

we are going to our dictionary of stacks and the indication and extract the data we need to move the creates. to do the actual moving part will do a range loop to simulate the  "one at the time" restriction while popping the creates from the stack we are moving from and inserting them into the stack we are moving to. remember that we are using a list to represent the stack so we will use the ```.insert()``` method with an index of 0 to insert the creates at the top of the stack.

```python
def move_create(create_stacks,indication):
  stack_from:list = create_stacks[str(indication[1])]
  stack_to:list = create_stacks[str(indication[2])]
  creates_qty = indication[0]
  for _ in range(creates_qty):
    stack_to.insert(0,stack_from.pop(0))
```

our code is almost done, we just need to iterate through the indications and call the ```move_create``` function for each one of them.

```python
 with open('./data.txt','r') as input:
    data = input.readlines()
    stacks = get_stacks(data)
    stacks_data = data[:data.index('\n')-1]
    crate_stacks = parse_stacks(stacks,stacks_data)
    indications_data=data[data.index('\n')+1:]
    indications = parse_indications(indications_data)
    for indication in indications:
      move_create(crate_stacks,indication)
```

and now we retrieve the first crate of each stack to get the flag
  
```python
  def get_first_crates(create_stacks):
  first_crates = []
  for stack in create_stacks.values():
    first_crates.append(stack[0])
  return first_crates

print("".join(get_first_crates(crate_stacks)))
```

## Part 2 

We will re-use almost everything from Part1 except the moving logic, now we can move more than one crate at the time, for this we will use list comprehension to extract the creates we need to move and then we will pop them using the same for loop we used earlier.
finally we need to append it to our data structure by the reference passed onto the function.

```python
def move_create_task2(create_stacks,indication):
  stack_from:list = create_stacks[str(indication[1])]
  stack_to:list = create_stacks[str(indication[2])]
  creates_qty = indication[0]
  creates = stack_from[:creates_qty]
  for _ in range(creates_qty):
    stack_from.pop(0)
  create_stacks[str(indication[2])] = creates + stack_to

```
This ends up in the following code 

```python
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
```