def isValidSubsequence(array, sequence):
    pointer = 0
    for ele in array:
        if ele == sequence[pointer]:
            pointer += 1
        if pointer == len(sequence):
            return True
    return False