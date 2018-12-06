input = open("01.in", "r")
data = input.read().splitlines()

# set of occured frequencies
frequencies = set()
sum = 0

# repeat until a frequency repeats
while True:
    # sum all frequencies
    for line in data:
        if sum in frequencies:  # if the frequency has already occured
            print(sum)
            quit()
        else:                   # if it hasn't
            frequencies.add(sum)

        sum += int(line)
