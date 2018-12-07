input = open("06.in", "r")
data = input.read().splitlines()

# get the points
points = []
for i in range(len(data)):
    coords = data[i].split(", ")
    points.append((int(coords[0]), int(coords[1])))

# find the maximum x and y values
maxX,maxY = max(points, key=lambda v:v[0])[0], max(points, key=lambda v:v[1])[1]

# go through each point on the board
pointFrequency = [0] * len(data)
for i in range(maxY + 1):
    for j in range(maxX + 1):
        miDist = float("+inf")
        minID = None

        # calculate distance from all points
        for k in range(len(points)):
            point = points[k]
            distance = abs(i - point[1]) + abs(j - point[0])

            # if there is a smaller distance, save that one instead
            # if two distances are equal, save neither (set id to None)
            if distance < miDist:
                miDist = distance
                minID = k
            elif distance == miDist:
                minID = None

        # if there is a closest point, either increment its frequency, or set
        # the frequency to -1 if it's on the edge
        if minID != None and pointFrequency[minID] != -1:
            if i == 0 or i == maxY or j == 0 or j == maxX:
                pointFrequency[minID] = -1
            else:
                pointFrequency[minID] += 1

print(max(pointFrequency))
