# Day 6

## Part 1

I have to say I've found this challenge easier than the previous one.

regarding the data parsing, there isn't anything fancy, just get the entire stream removing the EOL characters.

```python
data:list[str] = [line.removesuffix('\n') for line in input.readlines()]
```

We are looking for a pattern inside the stream of data. the first 4 consecutive characters sequence that don't repeat themselves, the answer is the number of characters after that sequence.

Let's iterate through the data stream and then over each character in it, in this case we are assuming there might be multiple data streams.

```python
for buffer in data:
    partial_buffer = ""
    for index,char in enumerate(buffer):
```

We are going to construct a partial buffer result out of the following condition:
  
  ```python
  partial_buffer = partial_buffer[1:] + "".join(buffer[index]) if len(partial_buffer) % 4 == 0 else partial_buffer + "".join(buffer[index])
  ```
this means, take the upcoming character in the buffer and add it to the partial buffer unless you've reached the 4th character inside the partial buffer, in that case remove the first one and add the new one, this way we are always keeping the last 4 characters in the partial buffer.

This partial buffer helps us think of a function with the following signature:
  
  ```python
  stop = check_flag(partial_buffer,index)
      if stop:
        break
  ```
the ````check_flag```` function  will check if the buffer is long enough and then we are doing some set magic to see if every character is unique

If you dont know about sets in python I highly recommend you to check them out, they are very useful.

```python
def check_flag(partial_buffer:list[str],index:int):
  if len(partial_buffer) < 4 :
    return 
  if(len(set(partial_buffer)) == len(partial_buffer)):
    print(index + 1)
    return True 
```

we are doing a ````+1```` on the index because we care about the number of characters not the index itself.

## Part 2 

Part 2 can be solved with the same ````check_flag```` function, the only difference is that we are going to check for a 14-characters pattern.

```python

partial_buffer = partial_buffer[1:] + "".join(buffer[index]) if len(partial_buffer) % 14 == 0 else partial_buffer + "".join(buffer[index])

def check_flag(partial_buffer,index):
    if len(partial_buffer) < 14 :
      return 
    if(len(set(partial_buffer)) == len(partial_buffer)):
      print(index + 1)
      return True
```
