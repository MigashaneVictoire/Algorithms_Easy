def isValidSubsequence(array, sequence):
    pointer = 0
    for ele in array:
        if ele == sequence[pointer]:
            pointer += 1
        if pointer == len(sequence):
            return True
    return False

def isValidSubsequence_sol2(array, sequence):
    arrPoint = 0
    seqPoint = 0
    while arrPoint < len(array):
        if array[arrPoint] == sequence[seqPoint]:
            seqPoint += 1
        if seqPoint == len(sequence):
            return True
        arrPoint += 1
    return False
        