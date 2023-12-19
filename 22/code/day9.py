class pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def add(self, direction: tuple[int, int]):
        self.x += direction[0]
        self.y += direction[1]
    def __str__(self):
        return f"({self.x}, {self.y})"

def move(direction: tuple[int, int]):
        global head, tail
        head.add(direction)

        if not touching(tail, head):
            sign_x = 0 if head.x == tail.x else (head.x - tail.x) / abs(head.x - tail.x)
            sign_y = 0 if head.y == tail.y else (head.y - tail.y) / abs(head.y - tail.y)
            sign = (sign_x, sign_y)
            tail.add(sign)

def move_tail(direction: tuple[int, int]):
        tails[0].add(direction)
        for i in range(9):
            hx = tails[i].x
            hy = tails[i].y
            tx = tails[i+1].x
            ty = tails[i+1].y
            if not touching(tails[i], tails[i+1]):
                sign_x = 0 if hx == tx else int((hx - tx) / abs(hx - tx))
                sign_y = 0 if hy == ty else int((hy - ty) / abs(hy - ty))
                sign = (sign_x, sign_y)
                tails[i+1].add(sign)


def touching(tail: pos, head: pos) -> bool:
    return (abs(head.x - tail.x) <= 1 and abs(head.y - tail.y) <= 1)



directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
head = pos(0, 0)
tail = pos(0, 0)
visited = set()
visited.add((tail.x, tail.y))

with open("input/day9.txt", "r") as f:
    lines = f.read().strip().splitlines()
    
for line in lines:
    line = line.split(" ")
    direction = directions[line[0]]
    length = int(line[1])
    
    for _ in range(length):
        move(direction)
        visited.add((tail.x, tail.y))

#print(len(visited))

# part 2
tails = [pos(0, 0) for _ in range(10)]
visited_by_tail9 = set()
visited_by_tail9.add((tails[9].x, tails[9].y))

for line in lines:
    line = line.split(" ")
    direction = directions[line[0]]
    length = int(line[1])
    
    for _ in range(length):
        move_tail(direction)
        visited_by_tail9.add((tails[9].x, tails[9].y))
print(visited_by_tail9)
print(len(visited_by_tail9))