from ast import literal_eval
from re import sub

regex = open("20.in", "r").read().splitlines()[0][1:-1]

directionToStep = {"E": (1, 0),
                   "N": (0, -1),
                   "S": (0, 1),
                   "W": (-1, 0)}

x, y = 0, 0
minX, minY, maxX, maxY = 0, 0, 0, 0
coordinateStack, moveDict = [], {}

# find coordinates of adjacent rooms
for char in regex:
    if char in "ENSW":  # direction - add the move to the "graph"
        direction = directionToStep[char]

        start = (x, y)
        x, y = x + direction[0], y + direction[1]
        end = (x, y)

        if start not in moveDict:
            moveDict[start] = []
        moveDict[start].append(end)
    elif char == "(":   # ( - add the current coords to the stack
        coordinateStack.append((x, y))
    elif char == "|":   # | - reset x and y to the last coord on stack
        coordinate = coordinateStack[-1]
        x, y = coordinate[0], coordinate[1]
    elif char == ")":     # ) - remove last coordinate from stack
        coordinate = coordinateStack.pop()
        x, y = coordinate[0], coordinate[1]


# run DFS on the graph
stack, explored = [(0, 0)], {(0, 0):0}
while len(stack) != 0:
    coord = stack.pop()

    # if it has adjacent rooms
    if coord in moveDict:
        for neighbour in moveDict[coord]:
            # if it has adjacent unexplored rooms
            if neighbour not in explored:
                explored[neighbour] = explored[coord] + 1
                stack.append(neighbour)

print(max([v for k, v in explored.items()]))
