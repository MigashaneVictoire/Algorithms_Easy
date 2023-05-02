# Solution 1
def tournamentWinner(competitions, results):
    winners = []
    for key, value in enumerate(competitions):
        if results[key] == 0:
            winners.append(value[1])
        elif results[key] == 1:
            winners.append(value[0])
    return max(winners, key= winners.count)

# Solution 2
def tournamentWinner_sol2(competitions, results):
    # Write your code here
    countPoint = []
    for key, value in enumerate(competitions):
        if results[key] == 0:
            countPoint.append(value[1])
        elif results[key] == 1:
            countPoint.append(value[0])
    return max(countPoint, key=countPoint.count)