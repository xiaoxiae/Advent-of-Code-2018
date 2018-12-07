from re import search

input = open("05.in", "r")
data = input.read().splitlines()[0]

# perform the reactions
i = 0
while i < len(data) - 1:
    # ascii letter number xor 32 is the same letter in opposite case
    if chr(ord(data[i]) ^ 32) == data[i + 1]:
        # shorten the string by 2
        data = data[0:i] + data[i+2:]

        # go back 1 index (to possible react something that was blocked)
        if i != 0:
            i -= 1
    else:
        i += 1

print(len(data))
