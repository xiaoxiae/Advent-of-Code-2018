input = open("08-0.in", "r")
data = list(map(int, input.read().splitlines()[0].split(" ")))


def sumTreeMetadata(start, tree):
    """Recursively sums of the metadata of the tree."""
    # sums the children of a node until it has no more children
    total = 0
    while tree[start] != 0:
        tree[start] -= 1
        total += sumTreeMetadata(start + 2, tree)

    # add the metadata of the node (with 0 children) and remove it
    total += sum(tree[start + 2: start + 2 + tree[start + 1]])
    tree[:] = tree[:start] + tree[start + 2 + tree[start + 1]:]

    return total


print(sumTreeMetadata(0, data))
