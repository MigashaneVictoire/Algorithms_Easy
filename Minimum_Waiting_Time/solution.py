# O(nlogn) time and O(1) space
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    totalTime = []
    running_time = 0
    for key in range(1, len(queries)):
        running_time += queries[key - 1]
        totalTime.append(running_time)

    return sum(totalTime)
