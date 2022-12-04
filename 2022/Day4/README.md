# Day 4

## Part 1

This is a good example of how sometimes some sketching can help you to easily break down a seemingly complex problem.

We are dealing with ranges of integer numbers, and our goal is to find the number of pairs that overlap. each part with a slight variation. 

The hard part is to find the if statement that will determine whether the two ranges overlap or not.

This is why I started by sketching the problem on a piece of paper and writing the ranges on the same scale, if you find yourself struggling with this part I highly suggest you do the same.

First, we start by reading the data out of the input file and parsing it into a list, of lists of tuples, each tuple will contain the start and end of the range. and we will have inside the same iterable both ranges to compare

To picture the data structure:

```python
[(2, 4), (6, 8)], [(2, 3), (4, 5)]]
```

- first, we remove the EOL character from each line
- then we split the line into two parts one for each range
- each of these parts must be split into two parts, one for the start and one for the end using the '-' character as a separator
```python
def get_pairs():
    with open('./data.txt', 'r') as input:
        data = [line.removesuffix('\n') for line in input.readlines()]
    parsed_data = []
    for line in data:
        pair = line.split(',')
        parsed_data.append(
            [
                (int(pair[0].split('-')[0]), int(pair[0].split('-')[1])),
                (int(pair[1].split('-')[0]), int(pair[1].split('-')[1]))
            ]
        )
    return parsed_data
```

For the first part, we are looking for ranges that completely overlap. We will start by checking which range is the smallest based on the start of each pair, this way we will know the start point of the overlap. Then we will check if the end of the smallest range is greater than the end of the largest range, if it is then we have a full overlap.

```python

def task1():
    overlapped_pairs = 0
    for pairs in get_pairs():
        min_pair = min(pairs, key=lambda x: x[0])
        if min_pair[1] >= max(pairs, key=lambda x: x[0])[1]:
            overlapped_pairs += 1
    return overlapped_pairs
```

And we get the result
  
```python
if __name__ == '__main__':
  print(task1())
```
## Part 2

For part 2 we look for pairs that overlap at all se the if statement is a bit different, we will check if the end of the smallest range is greater or equal to the start of the largest range, if it is then we have an overlap that not necessarily is complete.

```python
def task2():
    overlapped_pairs = 0
    for pairs in get_pairs():
        min_pair = min(pairs, key=lambda x: x[0])
        if min_pair[1] >= max(pairs, key=lambda x: x[0])[0]:
            overlapped_pairs += 1
    return overlapped_pairs
```

And we get the result

```python
if __name__ == '__main__':
    print(task2())
```