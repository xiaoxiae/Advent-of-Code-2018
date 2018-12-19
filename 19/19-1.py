class Register:
    """A class that functions as a register."""
    def __init__(self, value=0):
        self.value = value


# optcodes as lambda functions
optcodes = {
    "addr":  lambda reg, a, b: reg[a].value + reg[b].value,
    "addi":  lambda reg, a, b: reg[a].value + b,
    "mulr":  lambda reg, a, b: reg[a].value * reg[b].value,
    "muli":  lambda reg, a, b: reg[a].value * b,
    "banr":  lambda reg, a, b: reg[a].value & reg[b].value,
    "bani":  lambda reg, a, b: reg[a].value & b,
    "borr":  lambda reg, a, b: reg[a].value | reg[b].value,
    "bori":  lambda reg, a, b: reg[a].value | b,
    "setr":  lambda reg, a, b: reg[a].value,
    "seti":  lambda reg, a, b: a,
    "gtir":  lambda reg, a, b: int(a > reg[b].value),
    "gtri":  lambda reg, a, b: int(reg[a].value > b),
    "gtrr":  lambda reg, a, b: int(reg[a].value > reg[b].value),
    "eqir":  lambda reg, a, b: int(a == reg[b].value),
    "eqri":  lambda reg, a, b: int(reg[a].value == b),
    "eqrr":  lambda reg, a, b: int(reg[a].value == reg[b].value)
}


# get input
input = open("19.in", "r").read().splitlines()

# create the registers and bind the ip register
registers = [Register(0) for _x in range(6)]
ip = registers[int(input[0].split(" ")[1])]

# parse string instructions
instructions = []
for instruction in input[1:]:
    s = instruction.split(" ")
    instructions.append([optcodes[s[0]], int(s[1]), int(s[2]), int(s[3])])

# while ip is pointing at a valid instruction
while ip.value >= 0 and ip.value < len(instructions):
    instruction = instructions[ip.value]

    # perform the instruction operation
    registers[instruction[3]].value = \
        instruction[0](registers, instruction[1], instruction[2])

    ip.value += 1

print([r.value for r in registers][0])
