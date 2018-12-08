input = open("08.in", "r")
data = list(map(int, input.read().splitlines()[0].split(" ")))


def constructMetadataTree(start, tree):
    """Construct a metadata tree."""
    # the metadata of all the children of the node
    children = []
    while tree[start] != 0:
        tree[start] -= 1
        children.append(constructMetadataTree(start + 2, tree))

    # save its metadata and remove it
    node = tree[start + 2: start + 2 + tree[start + 1]]
    tree[:] = tree[:start] + tree[start + 2 + tree[start + 1]:]

    # return its metadata and the metadata of its children
    return [node, children]


def findRootValue(node):
    """Finds the value specified in the problem."""
    metadata, children = node[0], node[1]
    total = 0

    if len(children) == 0:  # no children -> return sum of metadata
        total += sum(metadata)
    else:                   # some children -> return sums of valid indexes
        for index in metadata:
            if index - 1 < len(children):   # -1 is because indexes start at 0
                total += findRootValue(children[index - 1])

    return total


tree = constructMetadataTree(0, data)   # construct the metadata tree
print(findRootValue(tree))              # find the required value
