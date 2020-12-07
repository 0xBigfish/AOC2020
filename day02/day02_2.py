# read the input file
with open("input", "r") as f:
    readContent = f.readlines()
    
 
# convert input to a list
# input of form: '4-11 v: vvvbvvvvvvnvvd'
input_List = []
passwordCounter = 0
for line in readContent:

    # remove the \n at the end of lines
    line = line.replace('\n', '')
    
    # get the range in which the char should occur in the string
    tuple = line.partition(" ")
    nRange = tuple[0]
    nMin = int(nRange.partition("-")[0])
    nMax = int(nRange.partition("-")[2])
    print(nMin , nMax)
    
    restString = tuple[2] # tuple[1] = " "
    
    # get the character itself
    tuple = restString.partition(":")
    char = tuple[0]
    restString = tuple[2] # tuple[1] = ":"
    #print(char)
    
    # remove the leading space (" ")
    password = restString.replace(" ","")
    print(password)
    
    # check if the password fulfills the requirements
    # char must occur exactly once, either at nMin 
    # !!!! the password index starts at 1 !!!!
    charIncluded = False
    if password[nMin-1] == char:
        charIncluded = True
        
    if password[nMax-1] == char:
        if charIncluded: # the char must not occur more than once
            continue; # skip to the next interation
        else:
            charIncluded = True
         
    
    # char must occur exactly once
    if charIncluded:
        passwordCounter += 1

print("Number of correct passwords: " , passwordCounter)      
    
    
