# Day3

## Part 1

Let's start by pointing out that if you know about sets theory you will get the hang of it pretty easily, although there is a catch, these are not, by definition sets, because the rucksacks might contain the same item more than once, so we will have to use a list as a data structure instead.

The first part can be broken down into 2 main problems, first, we need a way to split the rucksacks evenly, and second, we need a way to compare the items in each rucksack and see if they have an intersection.

First, we need to get the data out of the input file
```python
with open('./data.txt', 'r') as input:
    total_priority = 0
    data = input.readlines()
    for rucksack in data:
```
to split the rucksacks we can use list comprehension as follows

```python
def divide_rucksack(rucksack: list):
    first_part = rucksack[:len(rucksack)//2]
    second_part = rucksack[len(rucksack)//2:]
    return first_part, second_part
```

and the intersection can be obtained like this

```python
def get_intersection(first_part: list, second_part: list):
    intersection = []
    for item in first_part:
        if item in second_part:
            intersection.append(item)
    return set(intersection)
```

I know, it might not be the most efficient way to do it or the safest one, but I needed a quick solution

Now we add the priority of the items in the intersection to the total priority

```python
with open('./data.txt', 'r') as input:
    total_priority = 0
    data = input.readlines()
    for rucksack in data:
        first_part, second_part = divide_rucksack(rucksack)
        intersection = get_intersection(first_part, second_part)
        for value in intersection:
            total_priority += item_types_map[value]
```

to get the priority of each item we can use a dictionary

```python
item_types_map = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    ...
```
## Part 2 
we will re-use the same map as before
  
  ```python
  from task1 import item_types_map
  ```

What changes here is the way we iterate through the rucksacks, we need to compare them by groups of 3, and instead of dividing a rucksack into equal parts we are going to  find the intersection between the 3 of them

```python
def three_rucksacks_intersection(rucksack1: str, rucksack2: str, rucksack3: str):
    intersection = []
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            intersection.append(item)
    return set(intersection)
```

Again this might not be the most elegant code I've written, but I was aiming for a quick solution

```python
with open('./data.txt', 'r') as input:
    total_priority = 0
    data = [line.removesuffix('\n') for line in input.readlines()]
    for i in range(0, len(data), 3):
        intersection = three_rucksacks_intersection(
            data[i], data[i+1], data[i+2])
        for value in intersection:
            total_priority += item_types_map[value]
```
we can print out the total priority

```python
if __name__ == '__main__':
    print(total_priority)
```