from os import remove


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
def remove_end_of_line():
    for i in range(len(binaries)):
        binaries[i] = binaries[i].replace("\n","")
        
with open("3Puzzle/binaries.txt","r") as file:
    binaries = file.readlines()
    remove_end_of_line()
    
    oxigen_raiting=0
    co2_rating=0
    
    another_binaries=binaries
    for i in range(12):
        if len(binaries)==1:
            oxigen_raiting=int(binaries[0],2)
            print(f"oxygen generator rating: {oxigen_raiting}")
            break
        value = most_common_value(binaries,i)
        binaries=[numbers for numbers in binaries if numbers[i]==value]
        
    for i in range(12):
        if len(another_binaries)==1:
            co2_rating=int(another_binaries[0],2)
            print(f"CO2 scrubber rating: {co2_rating}")
            break
        value = least_common_value(another_binaries,i)
        another_binaries=[numbers for numbers in another_binaries if numbers[i]==value]
    print(f"Total: {oxigen_raiting*co2_rating}")
    
    
    