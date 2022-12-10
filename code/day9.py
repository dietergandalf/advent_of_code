
def move(direction: tuple[int, int], length: int):
    for _ in range(length):
        #print_field(grid)
        head.x += direction[0]
        head.y += direction[1]
        # if head is not adjacent to tail, move tail
        # check for diagonal movement
        if abs(head.x - tail.x) > 1 and abs(head.y - tail.y) == 1 or abs(head.x - tail.x) == 1 and abs(head.y - tail.y) > 1:
            tail.x += 1 if head.x > tail.x else -1
            tail.y += 1 if head.y > tail.y else -1
            visited.add((tail.x, tail.y))
        if not (abs(head.x - tail.x) == 1 and head.y == tail.y) and not (abs(head.y - tail.y) == 1 and head.x == tail.x) and not (abs(head.x - tail.x) == 1 and abs(head.y - tail.y) == 1):
            tail.x += direction[0]
            tail.y += direction[1]
            visited.add((tail.x, tail.y))


class pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


represent = {0: ".", 1: "#"}
directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
head = pos(0, 0)
tail = pos(0, 0)
start = pos(0, 0)
visited = set((0, 0))

# again, works for the test input, but not for the actual input
with open("input/day9.txt", "r") as f:
    lines = f.read().strip().splitlines()
    for line in lines:
        line = line.split(" ")
        direction = directions[line[0]]
        length = int(line[1])
        move(direction, length)

print(len(visited))