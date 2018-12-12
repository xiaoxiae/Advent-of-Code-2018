input = open("11.in", "r")
serial = int(input.read().splitlines()[0])

board = [[0] * 300 for _y in range(300)]

# calculate all of the power levels
for y in range(300):
    for x in range(300):
        powerLevel = int(str(((x + 10) * y + serial) * (x + 10))[-3]) - 5
        board[y][x] = powerLevel

# calculate sums of all 3x3 parts of the grid
maxSum, maxSumCoords = 0, ()
for y in range(298):
    for x in range(298):
        sum = 0

        # find the sum of the 3x3
        for i in range(3):
            for j in range(3):
                sum += board[y + i][x + j]

        # if sum is larger than the current largest
        if maxSum < sum:
            maxSum = sum
            maxSumCoords = (x, y)

print(str(maxSumCoords[0])+","+str(maxSumCoords[1]))
