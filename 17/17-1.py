from re import findall
from time import sleep

import sys
sys.setrecursionlimit(10000)


def bounds(x, y, world):
    """Find the bounds by either overflowing or hitting a wall."""
    minX, maxX = x, x
    minOverflow, maxOverflow = False, False

    # flow left
    while world[minX][y + 1] != 0 and world[minX][y + 1] != 2 and world[minX - 1][y] != 1:
        minX -= 1
    minOverflow = world[minX][y + 1] == 0 or world[minX][y + 1] == 2

    # flow right
    while world[maxX][y + 1] != 0 and world[maxX][y + 1] != 2 and world[maxX + 1][y] != 1:
        maxX += 1
    maxOverflow = world[maxX][y + 1] == 0 or world[maxX][y + 1] == 2

    return (minX, maxX, minOverflow, maxOverflow)


def recursion(x, y, world):
    """Recursively fill the tank."""
    # if we hit the bottom or other flowing water
    if y + 1 == len(world[x]) or world[x][y + 1] == 2:
        world[x][y] = 2
        return 1

    # if we can flow downwards, do so
    if world[x][y + 1] == 0:
        world[x][y] = 2
        recursion(x, y + 1, world)

    # if there is still water under us or clay after flowing down, flow sideways
    if world[x][y + 1] == 1 or world[x][y + 1] == 3:
        result = bounds(x, y, world)
        for flowX in range(result[0], result[1] + 1):
            # flowing water if either of the sides overflowed, still if not
            world[flowX][y] = 2 if (result[2] or result[3]) else 3

        # if either of the sides overflowed, recursively fall from that side
        if result[2]:
            recursion(result[0], y, world)
        if result[3]:
            recursion(result[1], y, world)
    return


input = open("17.in", "r")
data = input.read().splitlines()

rows, columns = [], []
for line in data:
    numbers = [int(number) for number in findall("\d+", line)]
    if line[0] == "x":
        columns.append(numbers)
    else:
        rows.append(numbers)

# get minimum and maximum x and y
minX = min([min(columns)[0]] + min([row[1:] for row in rows]))
maxX = max([max(columns)[0]] + max([row[1:] for row in rows])) + 1
minY = min([min(rows)[0]] + min([column[1:] for column in columns]))
maxY = max([max(rows)[0]] + max([column[1:] for column in columns])) + 1

# create the world
world = [[0] * (maxY - minY) for _x in range(maxX - minX)]

# add columns
for column in columns:
    for y in range(column[1], column[2] + 1):
        world[column[0] - minX][y - minY] = 1

# add rows
for row in rows:
    for x in range(row[1], row[2] + 1):
        world[x - minX][row[0] - minY] = 1

# fill the world with water
recursion(500 - minX, 0, world)

# count the total number of water
total = 0
for line in world:
    for num in line:
        if num == 2 or num == 3:
            total += 1

print(total)
