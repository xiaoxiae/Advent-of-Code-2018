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

# iterate until we find the generation that repeats forever
beginningIndex = -3     # the index of the plant that is first in the list
generation = 0          # which generation are we on
previousNumber = ""     # the previous numberic representation of the generation
while True:
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
    generation += 1

    # the numberical representation of the generation
    number = int("".join(map(str, map(int, input)))[:-2], 2)

    # check, whether the numberic representation doesn't repeat
    if number == previousNumber:
        # fast-forward the 5000000000 0 generations
        beginningIndex += 50000000000 - generation
        break

    previousNumber = number

# sum the result
total = 0
for i in range(len(input)):
    if input[i]:
        total += i + beginningIndex

print(total)
