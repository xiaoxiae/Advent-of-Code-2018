import bisect

input = open("07.in", "r")
data = input.read().splitlines()

# does the same as 07-1.py
predecessorNumber = {}
successors = {}

numberOfWorkers = 5

# same as 07-1.py, only the numbering starts at 0 instead of 1
for line in data:
    start, end = ord(line[5]) - 64, ord(line[36]) - 64

    # set default dict values for successors
    if start not in successors:
        successors[start] = []
    if end not in successors:
        successors[end] = []

    # set default dict values for predecessorNumber
    if start not in predecessorNumber:
        predecessorNumber[start] = 0
    if end not in predecessorNumber:
        predecessorNumber[end] = 0

    predecessorNumber[end] += 1
    successors[start].append(end)

# add the duration and the id of each step
list = [[k + 60, k] for k, v in predecessorNumber.items() if v == 0]

totalTime = 0
while len(list) != 0:
    # find time of the step that the workers will finish first
    minimumTaskTime = min(list[0:numberOfWorkers])[0]

    totalTime += minimumTaskTime

    # for locating the step that finished
    minIDPosition = -1

    # subtract its time from as many steps as there are workers (or list length)
    for i in range(min(numberOfWorkers, len(list))):
        list[i][0] -= minimumTaskTime

        # if the task finished, save its position in the list
        if list[i][0] == 0:
            minIDPosition = i

    minID = list.pop(minIDPosition)[1]

    # subtract 1 from the number of successors to steps that follow this step
    for successor in successors[minID]:
        predecessorNumber[successor] -= 1

        # if the step that follows has no more predecessors, add it to the list
        if predecessorNumber[successor] == 0:
            list.append([successor + 60, successor])

print(totalTime)
