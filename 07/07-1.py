import heapq

input = open("07.in", "r")
data = input.read().splitlines()

# number of steps that preceed a step
predecessorNumber = {}

# the steps that follow a step
succeessors = {}

for line in data:
    start, end = ord(line[5]) - 65, ord(line[36]) - 65

    # set default dict values for succeessors
    if start not in succeessors:
        succeessors[start] = []
    if end not in succeessors:
        succeessors[end] = []

    # set default dict values for predecessorNumber
    if start not in predecessorNumber:
        predecessorNumber[start] = 0
    if end not in predecessorNumber:
        predecessorNumber[end] = 0

    predecessorNumber[end] += 1
    succeessors[start].append(end)

# create the heap from the numbers that don't have any preceding steps
heap = [k for k, v in predecessorNumber.items() if v == 0]
heapq.heapify(heap)

# start removing steps in their alphabetical order
while len(heap) != 0:
    element = heapq.heappop(heap)
    print(chr(element + 65), end="")

    # subtract 1 from the step that our popped step perceeded
    for successor in succeessors[element]:
        predecessorNumber[successor] -= 1

        # if the said step has no more preceeding steps, add it to the heap
        if predecessorNumber[successor] == 0:
            heapq.heappush(heap, successor)
