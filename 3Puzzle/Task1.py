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
        

with open("3Puzzle/binaries.txt","r") as file:
    binaries = file.readlines()
    for i in range(len(binaries)):
        binaries[i] = binaries[i].replace("\n","")
    gamma_rate=""
    for i in range(len(binaries[0])):
        zeros=0
        ones=0
        for numbers in binaries:
            if numbers[i] == "0":
                zeros+=1
            else:
                ones+=1
        if zeros==ones:
            print("we have a problem")
        if zeros>ones:
            gamma_rate+="0"
        else:
            gamma_rate+="1"
    epsilon_rate=invert_bin_number(list(gamma_rate))
    gamma_rate=int(gamma_rate,2)
    epsilon_rate=int(epsilon_rate,2)
    print(f"gamma_rate: {gamma_rate}, epsilon_rate: {epsilon_rate}")
    print(f"result:{gamma_rate*epsilon_rate}")
            
            
        