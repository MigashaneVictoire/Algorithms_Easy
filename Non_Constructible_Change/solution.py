def nonConstructibleChange(coins):
    coins.sort()
    currChange = 0
    for i in coins:
        if i > (currChange + 1):
            return currChange + 1
        else:
            currChange += i
    return currChange + 1
