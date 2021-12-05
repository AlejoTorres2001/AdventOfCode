# Day1

**I think it was a good way to start this event.I wouldn't say this particular puzzle was crazy hard. I still think this is NOT the optimal solution but I'm going to share the process that led me to this solution**

## Working with the "raw" data

the first problem I came up with was How the hell I was going to work with nearly 3000 numbers spitted out of an HTTP endpoint
at first I thought of taking advantage of vs code multi cursors and just type "," once for every line so I can end up with a list.
this turned to be a bad idea because (at least on  my crappy Notebook) after the first 700 simultaneous cursors vscode starts to behave weird 
So the next thing I thought was working the data from a plain text file. This was the one I stuck with at the end
```python
with open("1Puzzle\messurements.txt","r") as file :
    messurements=file.readlines() #get all mesurements on an array

```
## The previous measurement

the next step wat to figure out the "previous measurement" thing
through all the iteration of the list of measurements (except the first one) you will need to keep track of the previous item you went through
```python
previous=0 #starts with a 0
```
now we iterate through the list
```python
for messures in messurements:
        numeric_messure= int(messures) #we need Numbers!
        if previous == 0:
            print(f"{numeric_messure}N/A - no previous measurement")
 ```
 
 Finally we need o actually count the times an actual messure is greater than the prev one
 It is important to Point out the fact that numeric_messure WILL be our previous meassurement for our next iteration!
 ```python
 for messures in messurements:
        numeric_messure= int(messures)
        if previous == 0:
            print(f"{numeric_messure}N/A - no previous measurement")
        elif numeric_messure > previous:
            print(f"{numeric_messure} (Increased)")
            counter +=1 
        elif numeric_messure < previous:
            print(f"{numeric_messure}(Decreased)")
        previous = numeric_messure
```
all that last is to print out the counter 
```python
    print(f"the number of messurements that incresed are:{counter}")

```

## Second Part!

Now this one had a little bit more spice, however, if you followed the previous explanation this won't be that hard
Let's talk about the "three-measurement sliding window", basically you need to think of them as sub-lists from that big measurements lists from the beginning
```python
for i in range(len(messurements)):
        window=[]
    for j in range(3):
                try:
                    window.append(int(messurements[i+j]))
                except:
                    window=[]
                    print("No more messurements")
                    break
```
We need to make groups of three starting form every one of the numbers in our big list, excep when there are NOT enought numbers ahead to make the group,that is why we use the try except block

we will use a flag variable to stop form iterating once we reached the point when we can not make more groups
```python

if flag:
            for j in range(3):
                try:
                    window.append(int(messurements[i+j]))
                except:
                    window=[]
                    print("No more messurements")
                    flag=False
                    break

```
now we need to add the numbers from each group so we can compare them 
```python
def add_numbers(li):
    total=0
    for numbers in li:
        total+=numbers
    return total
 ```
 we can use this helper function to get the total from  both prev and actual groups of meassurements
 
  ```python
  
 previous =[] # the prev group
 flag=True #init flag
 counter=0
  for i in range(len(messurements)):
        window=[]
        if flag:
            for j in range(3): 
                try:
                    window.append(int(messurements[i+j])) #the next 2 numbers
                except:
                    window=[]
                    print("No more messurements")
                    flag=False
                    break 
            previous_result=add_numbers(previous)
            result = add_numbers(window)
            if (result>previous_result and previous_result!=0):
                counter+=1
            previous=window #same as before
```
