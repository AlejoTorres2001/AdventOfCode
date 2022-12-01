# Day 8
**I found it quite difficult to understand this problem, especially because in part one we don't need anything of that fancy explanation nor the input signals, just the outputs
second, the example for part 2 was a bit distracting**

the basic idea is that we have a bunch of seven-segment displays, every single one of this segments are represented with a letter 
The puzzle says that the connections between what number is broadcasted and the actual segments that light up are messed up
so is our job to decode what signals represent that segment

in part 1 we only care about 1,4,7 and 8 these numbers uses an unique mount of segments to be displayed, which makes them easier to identify
until part 2 we are not going to mess with the decoding of the signals 
let's start by reading every line from the input file and separating it into 2 lists, our signals and our output numbers, the ones we care about at the end
so we are going to check the length of every single one of them and comparing to the actual amount of segments we need to display 1 4 7 or 8
```python
with open("8Puzzle\input.txt") as file:
    displays = [lines.strip("\n") for lines in file.readlines()]
counter=0
number_lenghts=[2,4,7,3]
for dp in displays:
    signals,outputs = dp.split("|")
    signals = signals.strip().split(" ")
    outputs = outputs.strip().split(" ")
    for output in outputs:
            if len(output) in number_lenghts:
                counter+=1     
print(f"Total amount of 1,4,7 and 8 : {counter}")   
```
## Second part!
now here is where it gets tricky
we are going to stick with the way we are treating the input data
but in addition to that, we are going to make a sorted tuple with all the combinations of segments used to represent every single number
this is going to come in handy to check if the actual combination we guessed is correct or not 
```python
with open("8Puzzle\input.txt") as file:
    displays = [lines.strip("\n") for lines in file.readlines()]
    
digits_key = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]

digits = tuple(sorted(digits_key))
```
now we are going to brute force this problem by trying every single permutation possible for connecting every display segment with every signal input 
```python
 for sigma in itertools.permutations("abcdefg"):
        key = {}
        for char in "abcdefg":
            key[char] = sigma["abcdefg".index(char)]
```
hen we are going to try and decode our signals with that possible combination if every number decoded correspond to one in the digits tuple that means we found a way of connecting the broadcasted  signals and the segments that actually works, 
```python
 possible_combination = []
        for signal in signals:
            decoded = ""
            for char in signal:
                decoded += key[char]
            decoded = "".join(sorted(decoded))
            possible_combination.append(decoded)
        possible_combination.sort()
 ```
so finally we are going to use it to decode our output numbers 
```python
 if tuple(possible_combination) == digits:
            decoded_outputs = []
            for output in outputs:
                decoded_output = ""
                for char in output:
                    decoded_output += key[char]
                decoded_output = "".join(sorted(decoded_output))
                decoded_outputs.append(digits_key.index(decoded_output))
 ```
 At last we need to sum up all the numbers
 ```python
             total += int("".join([str(i) for i in decoded_outputs]))
 ```
