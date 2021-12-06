# Day6
**Have you ever seen a lantern fish in person?  I didn't, guess I will have to settle with this image**
![lanternfish](http://www.seasky.org/deep-sea/assets/images/lanternfish-se41.jpg)

I found myself in my comfort zone with part 1, things fall off from conventional in part 2, at least if you are like me and don't have much experience  in the field of data science and exponential distributions

for reading the input data y opted for a list

```python
with open("6Puzzle/input.txt", "r") as file:
    ages = file.read()
    ages = [int(number) for number in ages if number != ',']
```
then we are going to repeat the entire process for every day  
for day in range(1, 81):
we are going to iterate through the list of ages first checking if we have a 0 days fish (wich means is ready to spawn a freshly new one) , in this case we will append his child at the end of our list
```python
for day in range(1, 81):
        for i in range(len(ages)):
            if ages[i] == 0:
                ages.append(8)
                ages[i] = 7
            if ages[i] != 0:
                ages[i] -= 1
            print(f"after {day} days: {ages}")
 ```
by doing this we need to reset the father's timer back to 7 
*Now the problem here says we don't need to  reset it back to 7 but to 6 because 0 counts as a day I decided to skip this tip because I generalize the case of new birth and a regular decrease in the timer in the next if block*
```python
if ages[i] != 0:
    ages[i] -= 1
 ```
finally, we just need to count how many fish we have in our list
```python
 total = len(ages)
    print(f"total: {total}")
```

## Second part!

here is where this approach starts to fall apart very quickly
part 2 just extends on the exponentially increasing rate of part 1, technically you could still brute force your way around however a much more efficient way to solve this is by using dictionaries

we are going to start by using a freq dictionary as our main  data structure, taking days as our key and the number of fishes that have that timer as our value 
```python
from collections import defaultdict

with open("6Puzzle/input.txt", "r") as file:
    data = file.read().strip().split(',')
    freq = defaultdict(int)
    for d in data:
        freq[int(d)] += 1
        
```
*defaultdicts allow us to reference keys we haven't created yet, creating them*
we will use a *new_freq* dictionary to count the occurrences of that day

```python
new_freq = defaultdict(int)

```
we have to iterate through the keys of our freq dictionaries to cover all counter possibilities 
```python
 for _ in range(1, 257):
        new_freq = defaultdict(int)
        for key in freq:
```
In case we have a 0 key 2 things are going to happen,first we will have a new born,we add that 0 key value to the value of the 6 key,(meaning the timer is reset), and then every single one of those 0 will spawn a fish with an 8 counter
```python
if key == 0:
                new_freq[6] += freq[key]
                new_freq[8] = freq[key]
```
if this is not the case we just move the value of that key to the previous value (like subtracting 1 from a counter in the list approach)
```python
 for _ in range(1, 257):
        new_freq = defaultdict(int)
        for key in freq:
            if key == 0:
                new_freq[6] += freq[key]
                new_freq[8] = freq[key]
            else:
                new_freq[key-1] += freq[key]
        freq = new_freq
```
Now we just need to retrieve the values of every key in freq
```python
total = 0
for key in freq:
    total += freq[key]
print(f"total: {total}")

```
