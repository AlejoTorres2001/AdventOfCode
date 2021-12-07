# Day7

**Now when the problem said every single crab had a submarine I imagined something like this**
![crab submarine](https://static.turbosquid.com/Preview/2019/06/28__07_16_05/01.pngEF498E8E-6104-47DD-9CC5-644CAF8E5411Default.jpg)

we start dealing with distance!
working with the input data was not hard, I constructed a list out of the whole .txt file parsing to integer and splitting by ","
```python
with open("7Puzzle\input.txt", "r") as file:
    data = file.read().strip("\n")
    positions = [int(x) for x in data.split(",")]
```

We have to keep record of the minimum amount of fuel  that is why  we start with a big number 
```python
import sys
min_fuel = sys.maxsize
```
to determine the actual position where we can align all of them together and using the minimum amount of fuel possible we have to compare one position against all the remaining ones, and calculate how much fuel does it takes to move every single submarine to there 
```python
for i in range(len(positions)):
        fuel=0
        for j in range(len(positions)):
            distance = abs(positions[i] - positions[j])
            fuel += distance
```
*Now you might think that maybe the position where this happens is one where there is no submarine already, that might be true, but for my input that was not the case apparently, and i just iterated through the list*

we have to check if the actual amount of fuel we just calculated is lower than the min amount of fuel we previously had 

```python
 if fuel < min_fuel:
            position = positions[i]
            min_fuel = fuel
```
the we just print the answer
```python
print(f"min amount of fuel is {min_fuel} to get to {position}")
```

## Second Part!

Now we are told that the consumption of fuel is not constant and it increases every time we move one spot 
this ends up forcing us to sum up every single number from 1 to the actual distance the submarine and that point is  

to calculate this  we are going to use another variable *part_fuel* and add that to the actual fuel necessary considering that point 
```python
for k in range(1,distance+1):
                part_fuel+=k
fuel += part_fuel
```
just like this

```python
for i in range(len(positions)):
        fuel=0
        for j in range(len(positions)):
            part_fuel=0
            distance = abs(positions[i] - positions[j])
            for k in range(1,distance+1):
                part_fuel+=k
            fuel += part_fuel
 ```
 * *we use abs value because we are dealing with distances*
 * *We do **distance+1** because we need to count to the distance number, including it*
            
