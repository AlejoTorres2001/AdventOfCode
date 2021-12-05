# Day 2
IMO  I've found this puzzle easier than the first one, probably because of python built-in string methods, however this does not mean that it stops being quite a good one to solve.

Just a quick mention to my go to way for working with the puzzle´s inputs:
as seen before we are using a .txt file to handle the puzzle´s inputs.
```python
with open("2Puzzle/commands.txt", "r") as file:
    commands = file.readlines()
```
we now just need to find the right command so it triggers the right procedure.
```python
 for cmd in commands:
        if "down" in cmd:
            pass
        if "up" in cmd:
            pass
        if "forward" in cmd:
            pass
```
the only "Tricky" part is,as mentioned in the puzzle´s instructions, that up and down commands works the opposite
```python
for cmd in commands:
        if "down" in cmd:
            depth += int(cmd.split(" ")[1])
        if "up" in cmd:
            depth -= int(cmd.split(" ")[1])
        if "forward" in cmd:
            horizontal_pos += int(cmd.split(" ")[1])
```
Finally we need to multiply our depth and horizontal position
```python
    with open("2Puzzle/commands.txt", "r") as file:
    commands = file.readlines()
    horizontal_pos = 0
    depth = 0
    for cmd in commands:
        if "down" in cmd:
            depth += int(cmd.split(" ")[1])
        if "up" in cmd:
            depth -= int(cmd.split(" ")[1])
        if "forward" in cmd:
            horizontal_pos += int(cmd.split(" ")[1])
    print(f"horizontal position: {horizontal_pos}. depth: {depth}")
    print(f"total:{horizontal_pos*depth}")
```

## Second Part!

This one comes with a tiny twist, introducing "aim",working the same way as depth did.

```python
horizontal_pos = 0
depth = 0
aim = 0
```
the onle difference is the way the forward command works.As explained in puzzle´s instructions 
*forward X does two things:*

* *It increases your horizontal position by X units.*

* *It increases your depth by your aim multiplied by X.*

```python
if "forward" in cmd:
    horizontal_pos += int(cmd.split(" ")[1])
    depth += aim*int(cmd.split(" ")[1])
```
