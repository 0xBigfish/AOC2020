with open("input", "r") as f:
    readContent = f.readlines()
    input_List = []
    
    for line in readContent:
        input_List.append(int(line.replace('\n', '')))
        
flag = False
for n1 in input_List:
    for n2 in input_List:
        if (n1 != n2) & (n1 + n2 == 2020):
            print("First number is: " , n1)
            print("Second number is: " , n2)
            print("Sum is :" ,n1 + n2)
            print("Product is: " , n1 * n2)
            flag = True
            break
            
    if(flag): 
        break
            
    