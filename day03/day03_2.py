# read input
with open("input", "r") as f:
    # reverse the list in order to have the most top line as
    # the last element of the list ( will be useful in the while loop)
    input = list(reversed(f.readlines()))


def main(stepsRight, stepsDown):
    # get the width of the map
    firstLine = input[0].replace("\n", "")
    width = len(firstLine)

    # get the length of the map
    length = len(input)

    # goal is reach PAST the bottom of the map
    # starting in the top left corner of the map
    currentY = length-1
    currentX = 0

    # init the tree counter
    treeCounter = 0


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
        if currentLine[currentX] == '#':
            treeCounter += 1
            

    # we reached the bottom when the loop is done
    print("Trees hit while skiing down: " , treeCounter)
    return treeCounter

if __name__ == "__main__":
    print("----------------------------------------")
    print("When Skiing 1 to the right, 1 down")
    var11 = main(1, 1)
    print("----------------------------------------")
    
    
    print("----------------------------------------")
    print("When Skiing 3 to the right, 1 down")
    var31 = main(3, 1)
    print("----------------------------------------")
    
    
    print("----------------------------------------")
    print("When Skiing 5 to the right, 1 down")
    var51 = main(5, 1)
    print("----------------------------------------")
    
    
    print("----------------------------------------")
    print("When Skiing 7 to the right, 1 down")
    var71 = main(7, 1)
    print("----------------------------------------")
    
    
    print("----------------------------------------")
    print("When Skiing 1 to the right, 2 down")
    var12 = main(1, 2)
    print("----------------------------------------")
    
    
    print("\n\n\n\n")
    print("Product of these values: ", (var11 * var31 * var51 * var71 * var12))
