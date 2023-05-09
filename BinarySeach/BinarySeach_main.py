# O(log(n)) time and O(log(n)) space
def binarySearch(array, target):
    # Write your code here.
    return binarySearchHelper(array, target, left=0, right=len(array) - 1)


def binarySearchHelper(array, target, left, right):
    middle = (right + left) // 2
    if left > right:
        return -1
    if array[middle] > target:
        return binarySearchHelper(array, target, left, middle - 1)
    elif array[middle] < target:
        return binarySearchHelper(array, target, middle + 1, right)
    else:
        return middle

# O(n) time and O(n) space
def binarySearch1(array, target):
    # Write your code here.
    left= 0
    right= len(array) -1
    while left <= right:
        middle = (right + left) // 2
        if array[middle] > target:
            right = middle - 1
        elif array[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1
