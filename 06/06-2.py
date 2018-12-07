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
total = 0
for i in range(maxX):
    for j in range(maxY):
        # calculate distance from all points
        distanceSum = 0
        for p in points:
            distanceSum += abs(i - p[0]) + abs(j - p[1])

        # if it's within the specified distance
        if distanceSum < 10000:
            total += 1

print(total)
