import heapq

input = open("13.in", "r")
data =  input.read().splitlines()

# the heap to hold carts (and to correctly move them)
carts = []

# possible cart moves
steps = ((1, 0), (0, 1), (-1, 0), (0, -1))

# for cleaner code
dirSymbols = [">", "^", "<", "v"]
turnSymbols = ["/", "\\"]
straightSymbols = ["-", "|"]
intersectionSymbol = "+"

for i in range(len(data)):
    # convert to list so we can edit the line
    data[i] = list(data[i])
    for j in range(len(data[i])):
        # if it's a cart
        if data[i][j] in dirSymbols:
            # add it to carts list
            # remember position, direction, crossing counter and what block we
            # are standing on (we assumed that the carts don't start at
            # crossings or intersections)
            heapq.heappush(carts, [j, i, 0, 0, "-"] if data[i][j] == ">" else\
                                  [j, i, 1, 0, "|"] if data[i][j] == "v" else\
                                  [j, i, 2, 0, "-"] if data[i][j] == "<" else\
                                  [j, i, 3, 0, "|"])


while True:
    newCarts = []

    while len(carts) != 0:
        # get the next cart to process
        cart = heapq.heappop(carts)

        # examine the piece that the cart is standing on
        if cart[4] == intersectionSymbol:    # intersection
            # reverse the direction and increment the intersection counter
            cart[2] = (cart[2] + cart[3] % 3 + 3) % 4
            cart[3] += 1
        elif cart[4] in turnSymbols:         # turn
            if cart[4] == "/":
                cart[2] += 3 if cart[2] == 0 or cart[2] == 2 else 1
            elif cart[4] == "\\":
                cart[2] += 1 if cart[2] == 0 or cart[2] == 2 else 3
            cart[2] %= 4
        elif cart[4] not in straightSymbols: # collision
            print(str(cart[0])+","+str(cart[1]))
            quit()

        # place the piece that the cart was standing on back on the grid
        data[cart[1]][cart[0]] = cart[4]

        # drive the cart in its direction
        step = steps[cart[2]]
        cart[0], cart[1] = cart[0] + step[0], cart[1] + step[1]

        # put the cart on the map so we know this particular spot is occupied
        cart[4] = data[cart[1]][cart[0]]
        data[cart[1]][cart[0]] = cart

        # add the cart back to the stack
        heapq.heappush(newCarts, cart)

    carts = newCarts
