from collections import Counter

input = open("02.in", "r")
data = input.read().splitlines()

twoTimes = 0
threeTimes = 0

for line in data:
    # the lengths of the grouped sorted items
    occurences = [len([k,]*v) for k,v in Counter(sorted(line)).items()]

    # add the occurences
    if 2 in occurences:
        twoTimes += 1
    if 3 in occurences:
        threeTimes += 1

print(twoTimes * threeTimes)
