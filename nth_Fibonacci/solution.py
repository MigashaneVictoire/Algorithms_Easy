def getNthFib(n):
    secPrevFib = 0
    mostprevFib = 1
    nthFib = 0

    if n == 1:
        return secPrevFib
    elif n == 2:
        return mostprevFib

    for iter in range(3, n + 1):
        nthFib = mostprevFib + secPrevFib
        secPrevFib = mostprevFib
        mostprevFib = nthFib
    return nthFib


def getNthFib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib1(n - 1) + getNthFib1(n - 1)


# O(n)
def getNthFib2(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n - 1, memoize) + getNthFib2(n - 2, memoize)
    return memoize[n]


def getNthFib3(n):
    # O(n) time and O(1)
    lasttwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lasttwo[0] + lasttwo[1]
        lasttwo[0] = lasttwo[1]
        lasttwo[1] = nextFib
        counter += 1
    return lasttwo[1] if n > 1 else lasttwo[0]
