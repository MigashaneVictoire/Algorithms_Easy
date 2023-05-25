# O(n) time and O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    array.sort()
    moves = array.count(toMove)
    for i in range(moves):
        array.remove(toMove)
        array.append(toMove)
    return array
