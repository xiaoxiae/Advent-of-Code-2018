from re import search

def react(data):
    """Returns the reacted string."""
    i = 0
    while i < len(data) - 1:
        # in ascii, letter xor 32 is the letter in other case
        if chr(ord(data[i]) ^ 32) == data[i + 1]:
            data = data[0:i] + data[i+2:]
            if i != 0:
                i -= 1
        else:
            i += 1
    return data

input = open("05.in", "r")
data = react(input.read().splitlines()[0])

# try all of the possible replacements
min = float("+inf")
for x in range(97, 123):
    # the reaction with a letter removed
    result = len(react(data.replace(chr(x), "").replace(chr(x).upper(), "")))

    if result < min:
        min = result

print(min)
