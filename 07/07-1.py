import heapq

input = open("07.in", "r")
data = input.read().splitlines()

connectionNumbers = {}
connections = {}

for line in data:
    start, end = ord(line[5]) - 65, ord(line[36]) - 65

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

# create the heap from the numbers that don't have any preceding steps
heap = [k for k, v in connectionNumbers.items() if v == 0]
heapq.heapify(heap)

# continue removing steps in their alphabetical order
while len(heap) != 0:
    element = heapq.heappop(heap)
    print(chr(element + 65), end="")

    # subtract 1 from the number of connections to steps that follow this step
    for connection in connections[element]:
        connectionNumbers[connection] -= 1

        # if the said step has no more connections, add it to the heap
        if connectionNumbers[connection] == 0:
            heapq.heappush(heap, connection)
