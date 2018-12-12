input = open("11.in", "r")
serial = int(input.read().splitlines()[0])

size = 300

def bound(x, y, board):
    return x >= 0 and y >= 0 and x < len(board[0]) and y < len(board)

board = [[0] * size for _y in range(size)]
areaTable = [[0] * size for _y in range(size)]

# calculate all of the power levels and the summed area table
for y in range(size):
    for x in range(size):
        board[y][x] = int(str(((x + 10) * y + serial) * (x + 10))[-3]) - 5

        # the value of the summed are table
        areaTable[y][x] = board[y][x]\
            + (areaTable[y - 1][x] if bound(x, y - 1, areaTable) else 0)\
            + (areaTable[y][x - 1] if bound(x - 1, y, areaTable) else 0)\
            - (areaTable[y - 1][x - 1] if bound(x - 1, y - 1, areaTable) else 0)

# go through all k x k grids
maxSum = 0
result = ""
for k in range(3, 300):
    # calculate all k x k areas in the grid
    for y in range(1, size - k):
        for x in range(1, size - k):
            sum = areaTable[y + k][x + k] + areaTable[y][x]\
                - areaTable[y + k][x] - areaTable[y][x + k]

            # if the sum is bigger than the previous max sum
            if sum > maxSum:
                maxSum, result = sum, str(x+1)+","+str(y+1)+","+str(k)

print(result)
