class file:
    name: str
    size: int
    def __init__(self, name: str, size: int, height: int = 0) -> None:
        self.size = size
        self.name = name
        self.height = height
    def __str__(self) -> str:
        return "  " * self.height + "-" + f"{self.name} (file, size={self.size})"

class node(file):
    content: list
    def __init__(self, name: str, root = None, height: int = 0) -> None:
        self.name = name
        self.size = 0
        self.content = []
        self.root = root
        self.height = height
    # add a file or node to the node
    def add(self, item):
        self.content.append(item)
        self.size += item.size
        if self.root:
            self.root.update()
        else:
            self.update()

    # find a node by name
    def find(self, name: str):
        if self.name == name:
            return self
        for item in self.content:
            if isinstance(item, node):
                found = item.find(name)
                if found:
                    return found
        return None

    def find_parent(self, iterator= None):
        if not self.root:
            return self
        if not iterator:
            iterator = self.root
        for item in iterator.content:
            if isinstance(item, node):
                if item is self:
                    return iterator
        for item in iterator.content:
            if isinstance(item, node):
                found = self.find_parent(item)
                if found:
                    return found
        return None

    def update(self):
        self.size = 0
        for item in self.content:
            if isinstance(item, node):
                item.update()
            self.size += item.size
    
    def __str__(self) -> str:
        s = "  " * self.height + "-" + f"{self.name} (dir, size={self.size})"
        for item in self.content:
            s += "\n" + item.__str__()
        return s


# read the input file and create a list of nodes and files with their sizes
# works for the example input but not for the real input
with open("input/day7.txt", "r") as f:
    lines = f.read().strip().splitlines()
    tree = node("/")
    current = tree
    for line in lines:
        if line[0] == "$":
            if line == "$ ls":
                continue
            elif line == "$ cd ..":
                print(current.name)
                current = current.find_parent()
            elif line == "$ cd /":
                current = tree
            else:
                print(line[5:])
                print(tree)
                current = current.find(line[5:])
        else:
            content = line.split()
            if content[0] == "dir":
                current.add(node(content[1], tree, current.height + 1))
            else:
                current.add(file(content[1], int(content[0]), current.height + 1))
    tree.update()
print(tree)

# part 1
# find all nodes that have a size of <= than 100_000
size = 100_000

def find_fitting_nodes(root: node, size: int) -> list[node]:
    nodes = []
    if root.size <= size and root.size > 0:
        nodes.append(root)
    for item in root.content:
        if isinstance(item, node):
            nodes += find_fitting_nodes(item, size)
    return nodes

small_nodes = find_fitting_nodes(tree, size)
summe = 0
print(len(small_nodes))
for node_x in small_nodes:
    summe += node_x.size
print(summe)
