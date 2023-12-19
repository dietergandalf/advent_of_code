X = 1
COUNTER = 0
importent_list = []
DRAW_POS = 0
pic = ""

def cycle(length):
    global X, COUNTER
    for _ in range(length):
        COUNTER += 1
        draw()
        if COUNTER == 20 or COUNTER == 60 or COUNTER == 100 or COUNTER == 140 or COUNTER == 180 or COUNTER == 220:
            importent_list.append((COUNTER, X))


def draw():
    global X, DRAW_POS, COUNTER, pic
    if DRAW_POS % 40 == 0:
        pic += "\n"
        DRAW_POS = 0
    if abs(X - DRAW_POS) <= 1:
        pic += "#"
    else:
        pic += "."
    DRAW_POS += 1

with open("input/day10.txt", "r")as f:
    lines = f.read().strip().splitlines()
    for line in lines:
        if line == "noop":
            cycle(1)
        else:
            cycle(2)
            instruction, value = line.split(" ")
            X += int(value)

summe = 0
for a, b in importent_list:
    summe += a * b
print(summe)
print(pic)