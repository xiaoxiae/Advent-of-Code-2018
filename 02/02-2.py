from collections import Counter

def differBy1(a, b):
    """Returns True if they differ by 1 and False otherwise."""
    difference = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            difference += 1
        if difference > 1:
            return False
    return True

input = open("02.in", "r")
data = input.read().splitlines()

# brute-force... all possibilities
for i in range(len(data)):
    for j in range(i + 1, len(data)):

        # if they differ by 1, print the matching characters
        if differBy1(data[i], data[j]):
            for k in range(len(data[i])):
                if data[i][k] == data[j][k]:
                    print(data[i][k], end="")
