from re import search

input = open("04.in", "r")
data = sorted(input.read().splitlines())

guardData = {}
i = 0

# find sleeping patters for all guards
while i < len(data):
    guardID = int(search("#[0-9]+ ", data[i]).group(0)[1:].strip())

    if not guardID in guardData:
        guardData[guardID] = [0] * 60

    i += 1
    while i < len(data):
        if "falls asleep" in data[i]:
            sleepStartTime = int(data[i][15:17])
            sleepEndTime = int(data[i + 1][15:17])

            # add the sleeping pattern for each guard
            for j in range(sleepStartTime, sleepEndTime):
                guardData[guardID][j] += 1

            i += 2
            continue
        break

# the sleepiest minute of the guard
sleepiestMinute = 0
guard = 0
for k, v in guardData.items():
    if max(v) > sleepiestMinute:
        sleepiestMinute, guard = max(v), k

print(guard * guardData[guard].index(sleepiestMinute))
