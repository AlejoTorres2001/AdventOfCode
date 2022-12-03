# Day 2

## Part 1

We are still working with linear data structures, but now there's is a twist, the input data is somewhat encrypted and we need to translate it into a common language.

I think that is the key to this problem in particular

We start by reading the input file as usual and separating the data from each play

```python
 with open('./data.txt', 'r') as input:
        data = input.read().splitlines()
        for line in data:
            op, you = line.split(' ')
``` 

Now, this is the part where it can get messy if you don't understand the encryption, you could end up with a bunch of nasty if statements and a lot of code, but there is a cleaner way to deal with this.

we can use a dictionary to map the encrypted data to a common language

```python
op_map = {'A': 'R', 'B': 'P', 'C': 'S'}
you_map = {'X': 'R', 'Y': 'P', 'Z': 'S'}
```

For the calculating the points part, we could use another dictionary as well, but I think the code is more readable if we use a simple if statement that reflects the rules of the game

First, we need to get, what I call offset, this will be how many points I earn based on what I've played

```python
 score_offset = 1 if you_move == 'R' else 2 if you_move == 'P' else 3 if you_move == 'S' else 0
 ```

Now we can calculate the points

  ```python
  if you_move == op_move:
        return 3 + score_offset
    if you_move == 'R' and op_move == 'S' or you_move == 'P' and op_move == 'R' or you_move == 'S' and op_move == 'P':
        return 6 + score_offset
    return 0 + score_offset
```
We will re-use this logic in Part 2

```python

def calculate_points(you_move, op_move):
    score_offset = 1 if you_move == 'R' else 2 if you_move == 'P' else 3 if you_move == 'S' else 0
    if you_move == op_move:
        return 3 + score_offset
    if you_move == 'R' and op_move == 'S' or you_move == 'P' and op_move == 'R' or you_move == 'S' and op_move == 'P':
        return 6 + score_offset
    return 0 + score_offset
```

and with a bit of code magic, we can make everything re-usable for part 2

```python

def get_plays(task_cb):
    scores = []
    with open('./data.txt', 'r') as input:
        data = input.read().splitlines()
        for line in data:
            op, you = line.split(' ')
            scores.append(task_cb(you, op))
    return scores
```
and we get the first result

```python
print(sum(get_plays(task1)))
```

## Part 2

Now there is a change in the rules, and the meaning of our input data changed.

We are going to borrow some things from part 1

```python
from task1 import get_plays, op_map, calculate_points
```
we need a way to know what move should we play based on every scenario, we can use a dictionary for that

```python
lose_map = {'P': 'R', 'R': 'S', 'S': 'P'}
win_map = {'R': 'P', 'P': 'S', 'S': 'R'}
```

With this, we can calculate our next move

```python
def calculate_play(op_play, play_should_end):
    if play_should_end == 'X':
        return lose_map[op_play]
    if play_should_end == 'Z':
        return win_map[op_play]
    return op_play
```
Finally our task2 callback function
  
  ```python
  def task2(play_should_end, op):
    op_play = op_map[op]
    my_play = calculate_play(op_play, play_should_end)
    return calculate_points(my_play, op_play)
```
the only thing that changed from part 1 is the way we get our play, the points calculation part is the same

```python
print(sum(get_plays(task2)))
```