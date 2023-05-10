# O(n) time and O91) space
def bubbleSort(array):
    isSorted = False
    counter = 0
    while isSorted is False:
        isSorted =True
        for left in range(len(array) - 1 - counter):
            if array[left] > array[left + 1]:
                shiftAndUpdate(left, left + 1, array)
                isSorted = False
        counter += 1
    return array


def shiftAndUpdate(left, right, array):
    array[left], array[right] = array[right], array[left]
    # rightidx = array[right]
    # array[right] = array[left]
    # array[left] = rightidx