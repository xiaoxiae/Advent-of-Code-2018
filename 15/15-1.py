from heapq import heapify, heappush, heappop
from collections import deque

def nextPosition(creature, map):
    """Returns the position to which to move the creature."""
    # dict of coordinates specifying how we got there
    visited = {(creature[0], creature[1]):None}

    # order of the BFS run (coordinates of the the tiles on the map)
    positions = deque([(creature[0], creature[1], 0)])

    while len(positions) != 0:
        # get the next step
        pos = positions.popleft()

        # attempt next steps
        for step in steps:
            # coords of the next possible step
            x, y = step[0] + pos[0], step[1] + pos[1]

            # add valid next steps to positions and visited
            # if we find an enemy, return
            if map[x][y] == 0:
                if (x, y) not in visited:
                    positions.append((x, y, pos[2] + 1))
                    visited[(x, y)] = (pos[0], pos[1])
                continue
            elif map[x][y] != 1 and creature[2] != map[x][y][2]:
                # if we're right next to the enemy creature, don't move
                if pos[2] == 0:
                    return (creature[0], creature[1])

                # trace back how we got to the enemy creature
                creatureOrigin = (pos[0], pos[1])
                while visited[visited[creatureOrigin]] != None:
                    creatureOrigin = visited[creatureOrigin]

                return creatureOrigin
    return (creature[0], creature[1])


input = open("15.in", "r")
stringMap = input.read().splitlines()

# lists that holds the information about the terrain and creatures
map = [[0] * len(stringMap) for _x in range(len(stringMap[0]))]
creatures = []
elfGnomeNumbers = [0, 0]

# the possible steps that the creatures can make
steps = [(-1, 0), (0, 1), (0, -1), (1, 0)]

# convert the map into something more useful
for x in range(len(stringMap)):
    for y in range(len(stringMap[x])):
        char = stringMap[x][y]

        if char == "#":
            map[x][y] = 1
        elif char == "G" or char == "E":
            # x coord, y coord, elf or gnome (true/false), hp left, ap
            creature = [x, y, True if char == "E" else False, 200, 3]
            creatures.append(creature)
            elfGnomeNumbers[int(creature[2])] += 1
            map[x][y] = creature

round = 0
while True:
    # build the combat order using a heap
    combatOrder = []
    for creature in creatures:
        heappush(combatOrder, creature)

    while len(combatOrder) != 0:
        # get the creature and its future position
        creature = heappop(combatOrder)
        creatureFuturePosition = nextPosition(creature, map)

        # if either of the creature types died out
        if min(elfGnomeNumbers) == 0:
            print(sum([x[3] for x in creatures]) * round)
            quit()

        # if the creature's dead, continue
        if creature[3] <= 0:
            continue

        # the current and future position of the creature
        x, y = creature[0], creature[1]
        newX, newY = creatureFuturePosition[0], creatureFuturePosition[1]

        # update the creature's coordinates
        map[x][y][0], map[x][y][1] = newX, newY

        # move the creature on the map
        map[x][y], map[newX][newY] = 0, map[x][y]

        # find an enemy to attack
        adjacentEnemies = []
        for step in steps:
            enemyX, enemyY = newX + step[0], newY + step[1]

            # if there is a creature there
            if map[enemyX][enemyY] != 0 and map[enemyX][enemyY] != 1:
                # if it's an enemy creature
                if map[enemyX][enemyY][2] != creature[2]:
                    enemy = map[enemyX][enemyY]
                    heappush(adjacentEnemies, (enemy[3], enemy[0], enemy[1]))

        # if there are enemies to attack, pick the one with the lowest HP
        if len(adjacentEnemies) != 0:
            # get its position and lower its hp
            enemyPosition = heappop(adjacentEnemies)
            enemy = map[enemyPosition[1]][enemyPosition[2]]
            enemy[3] -= creature[4]

            # if we killed it, remove it from:
            if enemy[3] <= 0:
                map[enemy[0]][enemy[1]] = 0             # the map
                del(creatures[creatures.index(enemy)])  # the creature array

                # increase the number of the creatures of its type
                elfGnomeNumbers[int(enemy[2])] -= 1

    round += 1
