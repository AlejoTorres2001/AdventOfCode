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
           