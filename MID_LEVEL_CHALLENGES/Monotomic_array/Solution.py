# O(n) time and O(1) space
def isMonotonic(array):
    if len(array) < 3:
        return True
    if array[0] < 0:
        monoCheck = sorted(array, reverse=True)
    else:
        monoCheck = sorted(array)

    return monoCheck == array


def isMonotonic1(array):
    nonIncreasing = True
    nonDecreasing = True
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            nonDecreasing = False
        if array[i] > array[i-1]:
            nonIncreasing = False
    return nonIncreasing or nonDecreasing


n = [[6,5],[2,3]]
print([2,3] in n)