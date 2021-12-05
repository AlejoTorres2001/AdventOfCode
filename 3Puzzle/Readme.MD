# Day3

**This one was quite fun, maybe the Second part can seem to be a little intimidating at first but when you get the hang of it, you realize it is no different than what We have already seen**

This one starts pretty much the same as the other, we are going to be using the same logic as before, to get our input data, but this time we NEED to get rid of EOL characters

```python
with open("3Puzzle/binaries.txt","r") as file:
    binaries = file.readlines()
    for i in range(len(binaries)):
        binaries[i] = binaries[i].replace("\n","")
```

Another handy thing to keep in mind is that *the length of the numbers is always the same*

We are going to get our gamma_rate by counting the number of 1s and zeros in the ith digit of every binary number

```python
gamma_rate=""
    for i in range(len(binaries[0])):
        zeros=0
        ones=0
        for numbers in binaries:
            if numbers[i] == "0":
                zeros+=1
            else:
                ones+=1
```
then we have to check whether the number of ones is greater than the number of zeros, if it is, we have to add a 1 to gamma_rate , if it is not, we add a 0
```python
 if zeros==ones:#What do we do?
            print("we have a problem") 
        if zeros>ones:
            gamma_rate+="0"
        else:
            gamma_rate+="1"
```
**Just for the record, the puzzle does not say anything about a tie, it wasn´t a problem**


Now we need to get our epsilon,we are going to use our gamma_rate to get it, by just "inverting" the binary number

```python
epsilon_rate=invert_bin_number(list(gamma_rate))
```

```python
def invert_bin_number(number):
    epsilon_rate=""
    for i in range(len(number)):
        if number[i] == '0':
            number[i]='1'
        else:
            number[i]='0'
    for digit in number:
        epsilon_rate+=digit
    return epsilon_rate
```

Finally we convert our epsilon_rate and gamma_rate to decimal numbers
```python
gamma_rate=int(gamma_rate,2)
epsilon_rate=int(epsilon_rate,2)
```
Again, I think that Python is handling a decent amount of work here

## Second Part!

The key here is to understand well the "bit criteria" that we are going to use to get our final answer

*The bit criteria depends on which type of rating value you want to find:*

*To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.

*To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.

Basically we are going to use the same logic as before, but this time filtering out the numbers that don´t match our criteria
```python
    for i in range(12):
        value = most_common_value(binaries,i)
        binaries=[numbers for numbers in binaries if numbers[i]==value]
```
```python
def most_common_value(binaries,position):
    zeros=0
    ones=0
    for numbers in binaries:
        if numbers[position]=='0':
            zeros+=1
        else:
            ones+=1
    if zeros>ones:
        return '0'
    else:
        return '1'  
```
Our break condition is that we have only one binary number left, which is the one we want to find

```python
for i in range(12):
        if len(binaries)==1:
            oxigen_raiting=int(binaries[0],2)
            print(f"oxygen generator rating: {oxigen_raiting}")
            break
        value = most_common_value(binaries,i)
        binaries=[numbers for numbers in binaries if numbers[i]==value]
```

The same goes for the CO2 scrubber rating
```python
 for i in range(12):
        if len(another_binaries)==1:
            co2_rating=int(another_binaries[0],2)
            print(f"CO2 scrubber rating: {co2_rating}")
            break
        value = least_common_value(another_binaries,i)
        another_binaries=[numbers for numbers in another_binaries if numbers[i]==value]
```
```python
def least_common_value(binaries,position):
    zeros=0
    ones=0
    for numbers in binaries:
        if numbers[position]=='0':
            zeros+=1
        else:
            ones+=1
    if zeros>ones:
        return '1'
    else:
        return '0' 
```
Just to mention, we are making a copy of our initial binaries list, so we can use it later, due to the overwriting of it
```python
another_binaries=binaries
```
All that is left is to get our answer
```python
    print(f"Total: {oxigen_raiting*co2_rating}")
```