def sortedSquareArray(array):
    squared = []
    for ele in array:
        squared.append(abs(pow(ele,2)))
    squared.sort()
    return squared


def sortedSquaredArray_sol2(array):
    # create a list the length of the array, fill the list with zeros
    zeros = [0 for _ in array]
    leftPoint = 0
    rightPoint = len(array) -1

    for ele in range(len(array)):
        squareLeft = pow(abs(array[leftPoint]),2)
        squareRight = pow(abs(array[rightPoint]),2)
    
        if squareLeft <= squareRight:
            zeros[ele] = squareLeft
            leftPoint += 1
        else:
            zeros[ele] = squareRight
            rightPoint -= 1
    zeros.sort()
    return zeros