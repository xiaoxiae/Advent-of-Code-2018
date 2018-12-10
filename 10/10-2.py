from re import findall

input = open("10.in", "r")
data = input.read().splitlines()

# convert all data to points
points = []
for line in data:
    points.append(list(map(int, findall("[-]*[0-9]+", line))))

# the minimum delta of the maximum and minimum x coordinate
minXDelta = float("inf")

# count the number of seconds
counter = 0

# move the points until we find the delta minimum
while True:
    xMin, xMax = float("inf"), -float("inf")
    for point in points:
        # move the points by their vectors
        point[0] += point[2]
        point[1] += point[3]

        # check for x minmaxes
        if xMin > point[0]:
            xMin = point[0]
        if xMax < point[0]:
            xMax = point[0]

    # one second just passed
    counter += 1

    # either adjust minXDelta, or we found the minimum
    if xMax - xMin < minXDelta:
        minXDelta = xMax - xMin
    else:
        print(counter - 1)
        quit()
