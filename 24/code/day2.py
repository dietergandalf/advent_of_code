with open("input/day2.txt") as f:
    lines = f.read().strip().split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
        lines[i] = [int(x) for x in lines[i]]

count = 0
for line in lines:
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
    if safe:
        count += 1
print(count)