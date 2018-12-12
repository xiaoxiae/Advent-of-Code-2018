from re import findall

class Marble:
    """A Marble object that stores the previous marble and the next marble."""
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

input = open("09.in", "r")
data = list(map(int, findall("[0-9]+", input.read().splitlines()[0])))

players = data[0]
turns = data[1]

playerScores = [0] * players

# create the starting marble and link it onto itself
currentMarble = Marble(0)
currentMarble.prev, currentMarble.next = currentMarble, currentMarble

# repeat until all marbles are taken
for i in range(1, turns * 100 + 1):
    if i % 23 == 0:
        # go 7 marbles back
        for j in range(6):
            currentMarble = currentMarble.prev

        # increment player score
        playerScores[(i - 1) % players] += currentMarble.value + i

        # remove the marble
        currentMarble.prev.next = currentMarble.next
        currentMarble.next.prev = currentMarble.prev
    else:
        # go by 2 forward
        currentMarble = currentMarble.next.next

        # create the new marble
        newMarble = Marble(i)

        # link the new marble
        newMarble.prev, newMarble.next = currentMarble, currentMarble.next
        currentMarble.next.prev = newMarble
        currentMarble.next = newMarble

print(max(playerScores))
