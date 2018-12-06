from re import search

input = open("05.in", "r")
data = input.read().splitlines()[0]

# perform the reactions (alters the string)
i = 0
while i < len(data) - 1:
    # in ascii, letter xor 32 is the letter in other case
    if chr(ord(data[i]) ^ 32) == data[i + 1]:
        data = data[0:i] + data[i+2:]
        if i != 0:
            i -= 1
    else:
        i += 1

print(len(data))
