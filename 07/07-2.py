import bisect

input = open("07.in", "r")
data = input.read().splitlines()

connectionNumbers = {}
connections = {}
numberOfWorkers = 5

# same as 07-1.py
for line in data:
    start, end = ord(line[5]) - 64, ord(line[36]) - 64

    # set default dict values for connections
    if start not in connections:
        connections[start] = []
    if end not in connections:
        connections[end] = []

    # set default dict values for connectionNumbers
    if start not in connectionNumbers:
        connectionNumbers[start] = 0
    if end not in connectionNumbers:
        connectionNumbers[end] = 0

    connectionNumbers[end] += 1
    connections[start].append(end)

# add the duration and the number of the step
list = [[k + 60, k] for k, v in connectionNumbers.items() if v == 0]

totalTime = 0
while len(list) != 0:
    # find time of the task that will end first
    minimumTaskTime = min(list[0:numberOfWorkers])[0]

    # subtract the minimum task time from as many tasks as there are workers
    totalTime += minimumTaskTime
    for i in range(min(numberOfWorkers, len(list))):
        list[i][0] -= minimumTaskTime

    # find the id of the task that has 0 time left and remove it
    minID = -1
    for i in range(len(list)):
        if list[i][0] == 0:
            minID = list.pop(i)[1]
            break

    # subtract 1 from the number of connections to steps that follow this step
    for connection in connections[minID]:
        connectionNumbers[connection] -= 1

        # if the said step has no more connections, add it to the list
        if connectionNumbers[connection] == 0:
            list.append([connection + 60, connection])

print(totalTime)
