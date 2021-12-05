def add_numbers(li):
    total=0
    for numbers in li:
        total+=numbers
    return total
with open("1Puzzle\messurements.txt","r") as file :
    messurements=file.readlines()
    previous =[]
    band=True
    counter=0
    for i in range(len(messurements)):
        window=[]
        if band:
            for j in range(3):
                try:
                    window.append(int(messurements[i+j]))
                except:
                    window=[]
                    print("No more messurements")
                    band=False
                    break 
            previous_result=add_numbers(previous)
            result = add_numbers(window)
            if (result>previous_result and previous_result!=0):
                counter+=1
            previous=window
            print(window)
    print("Result:",counter)
                
        
        