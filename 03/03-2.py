from re import compile

input = open("03.in", "r")
data = input.read().splitlines()

total = 0
board = [[-1] * 1000 for _x in range(1000)]
elfs = [True] * len(data)

# put all of the pieces of fabric on the board
for i in range(len(data)):
    line = data[i]

    s = compile(" @ |: ").split(line)
    start = tuple(map(int, s[1].split(",")))
    size = tuple(map(int, s[2].split("x")))

    # create the rectangle from data
    for x in range(start[0], start[0] + size[0]):
        for y in range(start[1], start[1] + size[1]):
            # if they overlap, remove the overlaping ones from elfs bool array
            if board[x][y] != -1:
                elfs[i], elfs[board[x][y]] = False, False
            else:
                board[x][y] = i

# print the index of one that didn't overlap (+1, since indexes start at 0)
print(elfs.index(True) + 1)
