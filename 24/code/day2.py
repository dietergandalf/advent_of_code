with open("input/day2.txt") as f:
    lines = f.read().strip().split("\n")
    for i, line in enumerate(lines):
        lines[i] = line.split(" ")
        lines[i] = [int(x) for x in lines[i]]

def is_safe(line):
    higher = True
    safe = True
    for i, x in enumerate(line):
        if i == 0:
            continue
        if i == 1:
            if x < line[i-1]:
                higher = False
            elif x == line[i-1]:
                safe = False
                break
        else:
            if higher and x < line[i-1]:
                safe = False
                break
            if not higher and x > line[i-1]:
                safe = False
                break
        if abs(x - line[i-1]) > 3 or abs(x - line[i-1]) < 1:
            safe = False
            break
    return safe

def a():
    count = 0
    for line in lines:
        if is_safe(line):
            count += 1
    print(count)

def b():
    count = 0
    for line in lines:
        if is_safe(line):
            count += 1
            continue
        for j in range(len(line)):
            test = line.copy()
            test.pop(j)
            if is_safe(test):
                count += 1
                break
    print(count)

#a()
b()
