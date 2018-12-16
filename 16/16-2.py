from re import findall


def optResultMatch(before, after, index, result):
    """Checks, whether the result of an opt code on a set of registers before
    match the result after."""
    return int(before[:index] + [result] + before[(index + 1):] == after)


def optcodeResults(b, a, i):
    """Return results of all of the opt codes."""
    return [optResultMatch(b, a, i[3], ocode(b, i)) for ocode in optcodes]


# the optcodes as lambda functions that take registers and instructions
optcodes = [lambda reg, inst: reg[inst[1]] + reg[inst[2]],          # addr
            lambda reg, inst: reg[inst[1]] + inst[2],               # addi
            lambda reg, inst: reg[inst[1]] * reg[inst[2]],          # mulr
            lambda reg, inst: reg[inst[1]] * inst[2],               # muli
            lambda reg, inst: reg[inst[1]] & reg[inst[2]],          # banr
            lambda reg, inst: reg[inst[1]] & inst[2],               # bani
            lambda reg, inst: reg[inst[1]] | reg[inst[2]],          # borr
            lambda reg, inst: reg[inst[1]] | inst[2],               # bori
            lambda reg, inst: reg[inst[1]],                         # setr
            lambda reg, inst: inst[1],                              # seti
            lambda reg, inst: int(inst[1] > reg[inst[2]]),          # gtir
            lambda reg, inst: int(reg[inst[1]] > inst[2]),          # gtri
            lambda reg, inst: int(reg[inst[1]] > reg[inst[2]]),     # gtrr
            lambda reg, inst: int(inst[1] == reg[inst[2]]),         # eqir
            lambda reg, inst: int(reg[inst[1]] == inst[2]),         # eqri
            lambda reg, inst: int(reg[inst[1]] == reg[inst[2]])]    # eqrr


input = open("16.in", "r")
data = input.read().splitlines()

# key is the number of the optcode, lambda is the function
optcodeMapping = {}

i, total = 0, 0
while data[i] != "":
    before = [int(number) for number in findall("\d+", data[i])]
    after = [int(number) for number in findall("\d+", data[i + 2])]
    instruction = [int(s) for s in data[i + 1].split(" ")]

    result = optcodeResults(before, after, instruction)

    # if only 1 optcode matches
    if sum(result) == 1:
        # add it to the optcodeMapping
        optcodeMapping[instruction[0]] = optcodes[result.index(1)]

        # replace it with a dummy function so it always fails the comparison
        optcodes[result.index(1)] = lambda _x, _y: None

    i += 4

# perform the program
registers = [0, 0, 0, 0]
for i in range(i + 2, len(data)):
    inst = [int(s) for s in data[i].split(" ")]

    registers[inst[3]] = optcodeMapping[inst[0]](registers, inst)

print(registers[0])
