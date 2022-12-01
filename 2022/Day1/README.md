# Day 1

### Part 1

As usual, the first ones are the easiest. although the key to most problems is to understand the input structure and parse it correctly so you can imprint your custom logic on top of it

in this case, we are dealing with a simple linear data structure, It might be tricky to parse due to the input's format but we can use it in our favor as a breaking condition

we start by reading the whole files, dumping each line inside an array.

```python
def get_elfs_items():
  with open('./data.txt', 'r') as input:
    data = input.readlines()
```

As I said we will look for those empty lines to break the input into chunks, so we can process each chunk independently (elf items)

```python
 for line in data:
            if (line == '\n'):
                elfs.append(sum(elf))
                elf = []
                continue
            elf.append(int(line.replace('\n', '')))
```
we are iterating through the array and if we find an empty line we append the sum of the current elf to the elfs array

finally, we just need the max out of them 
  
```python
  max(get_elfs_items())

```

### Part 2

we will re-use our logic to get the elves items

```python
from task1 import get_elfs_items
```

simple sorting and adding up the last 3 items will be enough

```python

elfs.sort()
print(sum(elfs[-3:]))
```
