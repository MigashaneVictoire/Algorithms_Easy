# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# O(n) time and O(1) space)
def productSum(array, level= 1):
    runningSum = 0
    for ele in array:
        if type(ele) is int:
            runningSum += ele
        else:
            runningSum += productSum(ele, level+1)
    return runningSum * level
