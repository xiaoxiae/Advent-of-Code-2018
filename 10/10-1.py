from re import findall

input = open("10.in", "r")
data = input.read().splitlines()

# convert all data to points
points = []
for line in data:
    points.append(list(map(int, findall("[-]*[0-9]+", line))))

# the minimum delta of the maximum and minimum x coordinate
minXDelta = float("inf")

# move the points until we find the delta minimum
while True:
    xMin, xMax = float("inf"), -float("inf")
    yMin, yMax = float("inf"), -float("inf")
    for point in points:
        # move the points by their vectors
        point[0] += point[2]
        point[1] += point[3]

        # check for x and y minmaxes
        if xMin > point[0]:
            xMin = point[0]
        if xMax < point[0]:
            xMax = point[0]

        if yMin > point[1]:
            yMin = point[1]
        if yMax < point[1]:
            yMax = point[1]

    if xMax - xMin < minXDelta:
        minXDelta = xMax - xMin
    else:
        # move the points back 1 step (that was the minimal delta)
        xMin, xMax = float("inf"), -float("inf")
        yMin, yMax = float("inf"), -float("inf")
        for point in points:
            # move the points by their vectors backwards
            point[0] -= point[2]
            point[1] -= point[3]

            # check for x and y minmaxes
            if xMin > point[0]:
                xMin = point[0]
            if xMax < point[0]:
                xMax = point[0]

            if yMin > point[1]:
                yMin = point[1]
            if yMax < point[1]:
                yMax = point[1]

        # build the board to display the message on
        board = [[0] * (minXDelta + 1) for _x in range(yMax - yMin + 1)]

        # set the points on the board accordingly
        for point in points:
            board[point[1] - yMin][point[0] - xMin] = 1

        # prettyprint the board
        for row in board:
            for num in row:
                if num == 0:
                    print(" ", end="")
                else:
                    print("*", end="")
            print()
        quit()
