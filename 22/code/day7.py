class file:
    name: str
    size: int
    def __init__(self, name: str, size: int, height: int = 0) -> None:
        self.size = size
        self.name = name
        self.height = height
    def __str__(self) -> str:
        return "  " * self.height + "- " + f"{self.name} (file, size={self.size})"

class node(file):
    content: list
    def __init__(self, name: str, root = None, height: int = 0) -> None:
        self.name = name
        self.size = 0
        self.content = []
        self.root = root
        self.height = height
    # add a file or node to the node
    def add(self, item: file, path: list) -> None:
        self.content.append(item)
        for Node in path:
            Node.size += item.size

    # find a node by name
    def find(self, name: str) -> file:
        if self.name == name:
            return self
        for item in self.content:
            if isinstance(item, node):
                found = item.find(name)
                if found:
                    return found
        return None

    def __str__(self) -> str:
        s = "  " * self.height + "- " + f"{self.name} (dir, size={self.size})"
        for item in self.content:
            s += "\n" + item.__str__()
        return s

def find_fitting_nodes(root: node, size: int, compare_mode: str) -> list[node]:
    nodes = []
    if compare_mode == "smaller" and root.size <= size:
        nodes.append(root)
    elif compare_mode == "bigger" and root.size >= size:
        nodes.append(root)
    for item in root.content:
        if isinstance(item, node):
            nodes += find_fitting_nodes(item, size, compare_mode)
    return nodes

# read the input and build the tree
with open("input/day7.txt", "r") as f:
    lines = f.read().strip().splitlines()
tree = node("/")
path = [tree]
current = tree
for line in lines:
    if line[0] == "$":
        if line == "$ ls":
            continue
        elif line == "$ cd ..":
            path.pop()
            current = path[-1]
        elif line == "$ cd /":
            path = [tree]
        else:
            current = current.find(line[5:])
            path.append(current)
    else:
        content = line.split()
        if content[0] == "dir":
            current.add(node(content[1], tree, current.height + 1), path)
        else:
            current.add(file(content[1], int(content[0]), current.height + 1), path)

# part 1
# find all nodes that have a size of <= than 100_000
size = 100_000
small_nodes = find_fitting_nodes(tree, size, "smaller")
summe = 0
for node_x in small_nodes:
    summe += node_x.size
print(summe) # should be 1453349, is 1159272


# part 2

unused = 70_000_000 - tree.size
required = 30_000_000 - unused
big_nodes = find_fitting_nodes(tree, required, "bigger")
smallest = big_nodes[0]
for Node in big_nodes:
    if Node.size < smallest.size:
        smallest = Node
print(smallest.name, smallest.size)
