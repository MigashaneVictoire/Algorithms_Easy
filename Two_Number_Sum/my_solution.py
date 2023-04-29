# solution 1
def twoNumberSum(array, targetSum):
    array.sort()
    leftPoint = 0
    rightPoint = len(array) -1

    for i in range(len(array)):
        sum = array[leftPoint] + array[rightPoint]
        if sum < targetSum:
            leftPoint += 1
        elif sum > targetSum:
            rightPoint -= 1
        else:
            return [array[leftPoint], array[rightPoint]]
    return []

# solution 2
def twoNumberSum_sol2(array, targetSum):
    array.sort()
    leftPoint = 0
    rightPoint = len(array) -1

    while leftPoint < rightPoint:
        sum = array[leftPoint] + array[rightPoint]
        if sum < targetSum:
            leftPoint += 1
        elif sum > targetSum:
            rightPoint -= 1
        else:
            return [array[leftPoint], array[rightPoint]]
    return []