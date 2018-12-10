from re import findall

input = open("09.in", "r")
data = list(map(int, findall("[0-9]+", input.read().splitlines()[0])))

marbles = [0]
currentMarble = 0

currentPlayer = 0
playerScores = [0] * data[0]

# Simulate the turns
for i in range(1, data[1] + 1):
    if i % 23 == 0:     # if divisible, shift position back and increment score
        currentMarble = (currentMarble - 7 + len(marbles)) % len(marbles)
        playerScores[currentPlayer] += i + marbles.pop(currentMarble)
    else:               # shift position forward and add a marble
        currentMarble = (currentMarble + 1) % (len(marbles)) + 1
        marbles.insert(currentMarble, i)

    currentPlayer = (currentPlayer + 1) % len(playerScores)

print(max(playerScores))
