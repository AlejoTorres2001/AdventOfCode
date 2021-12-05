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
