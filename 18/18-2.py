input = open("18.in", "r")
data = input.read().splitlines()


def mapToString(world):
    return "".join(["".join(list(map(str, line))) for line in world])


def inBounds(x, y, world):
    """Returns True if coordinates are in bounds and False if they are not."""
    return x >= 0 and y >= 0 and x < len(world) and y < len(world[0])


def neighbourhood(x, y, world):
    """Returns the frequency of elements appearing around a coordinate."""
    steps = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
    neighbours = [0, 0, 0]

    # move in each direction
    for step in steps:
        newX, newY = x + step[0], y + step[1]
        if inBounds(newX, newY, world):
            neighbours[world[newX][newY]] += 1

    return neighbours


# number of generations
numberOfGenerations = 1000000000

# convert the world to a 2D numberical array
world = [[0] * len(data) for _x in range(len(data[0]))]
for y in range(len(data)):
    for x in range(len(data[y])):
        world[x][y] = 1 if data[x][y] == '|' else 2 if data[x][y] == "#" else 0

# a dictionary that stores the string representation of the generation
genDict = {}
generation = 0

while mapToString(world) not in genDict:
    newWorld = [[0] * len(data) for _x in range(len(data[0]))]

    # for each cell
    for y in range(len(data)):
        for x in range(len(data[y])):
            neighbours = neighbourhood(x, y, world)

            # perform the change onto the new array
            if world[x][y] == 0 and neighbours[1] >= 3:
                newWorld[x][y] = 1
            elif world[x][y] == 1 and neighbours[2] >= 3:
                newWorld[x][y] = 2
            elif world[x][y] == 2 and (neighbours[2] == 0 or neighbours[1] == 0):
                newWorld[x][y] = 0
            else:
                newWorld[x][y] = world[x][y]

    genDict[mapToString(world)] = generation
    generation += 1
    world = newWorld

# the start and end of the cycle
cycleStart = genDict[mapToString(world)]
cycleEnd = generation

# how many generations are left
cycleIndex = (numberOfGenerations - cycleStart) % (cycleEnd - cycleStart)

# find and sum the generation whose index in the cycle matches last generation
trees, lumberjacks = 0, 0
for k, v in genDict.items():
    if v - cycleStart == cycleIndex:
        for number in k:
            if number == "1":
                trees += 1
            elif number == "2":
                lumberjacks += 1

print(trees * lumberjacks)
