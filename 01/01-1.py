input = open("01.in", "r")
data = input.read().splitlines()

# sum the lines converted to integers
print(sum(map(int, data)))
