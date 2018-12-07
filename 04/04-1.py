from re import search

input = open("04.in", "r")
data = sorted(input.read().splitlines())

guardData = {}

# count the total times that the guards spent asleep (and when that was)
i = 0
while i < len(data):
    guardID = int(search("#[0-9]+ ", data[i]).group(0)[1:].strip())

    if not guardID in guardData:
        guardData[guardID] = [0, []]

    # sum the lengts and add durations the guard spent asleep to the dictionary
    i += 1
    while i < len(data):
        if "falls asleep" in data[i]:
            sleepStartTime = int(data[i][15:17])
            sleepEndTime = int(data[i + 1][15:17])

            # index 0 is for total time spent asleep, 1 is for the periods
            guardData[guardID][0] += sleepEndTime - sleepStartTime
            guardData[guardID][1].append((sleepStartTime, sleepEndTime))

            i += 2
            continue
        break

# find the guard that spent the most time asleep
sleepiestGuardID = sorted([(v[0], k) for k, v in guardData.items()])[-1][1]

# find the sleeping pattern
sleepiestGuardData = [0] * 60
for sleep in guardData[sleepiestGuardID][1]:
    for i in range(sleep[0], sleep[1]):
        sleepiestGuardData[i] += 1

# find the minute the guard spent the most time asleep
minute = sleepiestGuardData.index(max(sleepiestGuardData))

print(minute * sleepiestGuardID)
