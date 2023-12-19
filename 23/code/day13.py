def solve(file, part=1):
    with open(file, 'r') as f:
        data = f.readlines()
    part = []
    maps = []
    for line in data:
        if line.strip() == "":
            maps.append(part)
            part = []
            continue
        part.append(line.strip())
    maps.append(part)

    multiplier = 100

    sum = 0
    for map in maps:
        for ri in range(1,len(map)):
            mirror = True
            maxCount = min(ri, len(map)-ri-1)
            for i in range(0, maxCount+1):
                if map[ri-i-1] != map[ri+i]:
                    mirror = False
                    break
            if mirror:
                sum += ri * multiplier
                break

        possibleMirrorIndexes = [i for i in range(1, len(map[0]))]
        for line in map:
            for i in possibleMirrorIndexes:
                maxCount = min(i, len(line)-i-1)
                for j in range(0, maxCount+1):
                    if line[i-j-1] != line[i+j]:
                        possibleMirrorIndexes.remove(i)
                        break

        if len(possibleMirrorIndexes) > 0:
            sum += possibleMirrorIndexes[0]

    print(sum)


def findMirror(grid):
    for r in range(1,len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[:len(below)]
        below = below[:len(above)]
        if above == below:
            return r
    return 0

def findSmudgedMirror(grid):
    for r in range(1,len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        #if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
        #    return r
        
        summs = []
        for x, y in zip(above, below):
            s1 = sum(0 if a == b else 1 for a, b in zip(x, y))
            summs.append(s1)
        if sum(summs) == 1:
            return r

    return 0

def solveCorrect(file, part=1):
    total = 0
    for block in open(file).read().split("\n\n"):
        grid = block.splitlines()
        if part == 2:
            row = findSmudgedMirror(grid)
        else:
            row = findMirror(grid)
        total += row * 100

        if part == 2:
            col = findSmudgedMirror(list(zip(*grid)))
        else:
            col = findMirror(list(zip(*grid)))
        total += col
    print(total)


solveCorrect("23/input/day13_test.txt", 2)
solveCorrect("23/input/day13.txt", 2)
#solve("23/input/day13.txt", 1)
