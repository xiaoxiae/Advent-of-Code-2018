from re import compile

input = open("03.in", "r")
data = input.read().splitlines()

total = 0
board = [[0] * 1000 for _x in range(1000)]

# put all of the pieces of fabric on the board
for line in data:
    s = compile(" @ |: ").split(line)
    start = tuple(map(int, s[1].split(",")))
    size = tuple(map(int, s[2].split("x")))

    # create the fabric rectangle
    for x in range(start[0], start[0] + size[0]):
        for y in range(start[1], start[1] + size[1]):
            board[x][y] += 1

            # if they overlap, increment the total
            if board[x][y] == 2:
                total += 1

print(total)
