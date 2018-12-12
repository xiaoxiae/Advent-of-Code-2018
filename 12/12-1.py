input = open("12.in", "r")
data =  input.read().splitlines()

# get the input from tile and extend it
input = [True if c == "#" else False for c in data[0].split(" ")[2]]
input = [False] * 3 + input + [False] * 3

# convert rules that produce plats to a set
rules = set()
for rule in data[2:]:
    rule = rule.split(" => ")

    # ignore rules that don't produce plants and add those that do to the set
    if rule[1] == ".":
        continue
    else:
        configuration = tuple(True if c == "#" else False for c in rule[0])
        rules.add(configuration)

# iterate over 20 generations
beginningIndex = -3
for i in range(20):
    # resize the input array if necessary
    if input[2]:
        input = [False] + input
        beginningIndex -= 1
    if input[-3]:
        input = input + [False]

    # create the next generation
    newInput = [False] * len(input)
    for j in range(2, len(input) - 1):
        if tuple(input[j-2:j+3]) in rules:
            newInput[j] = True

    input = newInput

# sum the result
total = 0
for i in range(len(input)):
    if input[i]:
        total += i + beginningIndex

print(total)
