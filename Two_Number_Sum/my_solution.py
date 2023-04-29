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

# solution 3
def twoNumberSum_sol3(array, targetSum):
    array.sort()
    for i in array:
        for n in array[1:]:
            sum = i + n
            if sum == targetSum:
                return [i, n]
    return []