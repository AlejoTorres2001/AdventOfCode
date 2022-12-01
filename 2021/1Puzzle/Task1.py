with open("1Puzzle\messurements.txt","r") as file :
    messurements=file.readlines()
    previous=0
    counter =0
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
    print(f"the number of messurements that incresed are:{counter}")