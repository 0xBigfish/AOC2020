# read input
with open("input", "r") as f:
    # reverse the list in order to have the most top line as
    # the last element of the list ( will be useful in the while loop)
    input = list(reversed(f.readlines()))

# get the width of the map
firstLine = input[0].replace("\n", "")
width = len(firstLine)
print("Width: ", width)

# get the length of the map
length = len(input)
print("Length: ", length)


# ski down the map 
stepsRight = 3
stepsDown = 1

# goal is reach PAST the bottom of the map
# starting in the top left corner of the map
currentY = length-1
currentX = 0

# init the tree counter
treeCounter = 0

print("Current Pos ",currentY, ", ", currentX)

# start skiing
while(currentY > 0):
    
    # move to the right
    for i in range(1, stepsRight+1):
        currentX += 1
        
        # check if we droppedd out at the right,
        # then drop back in on the left
        if currentX < 0 or currentX >= width :
            currentX = 0
    
    # move down
    for i in range(1, stepsDown+1):
        currentY = currentY - 1
        
        
    # check if the field we land on is a tree
    currentLine = input[currentY]
    #print(currentLine)
    #print(currentX)
    if currentLine[currentX] == '#':
        treeCounter += 1
        print("Hit tree!")
        
    print("Current Pos ",currentY, ", ", currentX)

# we reached the bottom when the loop is done
print("Trees hit while skiing down: " , treeCounter)

