def tournamentWinner(competitions, results):
    winners = []
    for key, value in enumerate(competitions):
        if results[key] == 0:
            winners.append(value[1])
        elif results[key] == 1:
            winners.append(value[0])
    return max(winners, key= winners.count)