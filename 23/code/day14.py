def tiltCycle(grid):
    dirs = ["N", "W", "S", "E"]
    for dir in dirs:
        grid = tilt(grid, dir)
    return grid

def tilt(grid, dir):
    if dir == "N":
        for _ in range(len(grid)):
            for index in range(len(grid)-1, 0, -1):
                for i, char in enumerate(grid[index]):
                    if char != "O":
                        continue
                    if grid[index-1][i] == ".":
                        grid[index][i] = "."
                        grid[index-1][i] = "O"
        return grid
    elif dir == "S":
        for _ in range(len(grid)):
            for index, line in enumerate(grid):
                for i, char in enumerate(line):
                    if char != "O" or index == len(grid)-1:
                        continue
                    if grid[index+1][i] == ".":
                        grid[index][i] = "."
                        grid[index+1][i] = "O"
    elif dir == "W":
        for _ in range(len(grid[0])):
            for index, line in enumerate(grid):
                for i in range(len(line)-1, 0, -1):
                    if line[i] != "O":
                        continue
                    if grid[index][i-1] == ".":
                        grid[index][i] = "."
                        grid[index][i-1] = "O"
    elif dir == "E":
        for _ in range(len(grid[0])):
            for index, line in enumerate(grid):
                for i, char in enumerate(line):
                    if char != "O" or i == len(line)-1:
                        continue
                    if grid[index][i+1] == ".":
                        grid[index][i] = "."
                        grid[index][i+1] = "O"
    return grid

def solve(file, part=1):
    with open(file) as f:
        grid = f.read().splitlines()
    grid = [list(line) for line in grid]

    if part == 2:
        cycles = 1_000_000_000
        seen = {str(grid)}
        array = [grid]
        iter = 0
        while True:
            iter += 1
            grid = tiltCycle(grid)
            
            if str(grid) in seen:
                break
            else:
                seen.add(str(grid))
                array.append(grid)
        first = array.index(grid)
        cycle = iter - first
        grid = array[(cycles-first)%cycle+first]
    else:
        grid = tilt(grid, "N")
    

    sum = 0
    for i, line in enumerate(grid):
        sum += (len(grid)-(i)) * line.count("O")
    print(sum)
    

def solveWithTuples(file, part=1):
    grid = tuple(open(file).read().splitlines())

    def cycle(grid):
        for _ in range(4):
            grid = tuple(map("".join, zip(*grid)))
            grid = tuple("#".join(["".join(sorted(list(group), reverse=True)) for group in line.split("#")]) for line in grid) # magic to make the movable tiles fall down
            # this works by splitting the string at "#" and then sorting the characters in each group in reverse order- then joining the groups back together with "#" in between
            grid = tuple(row[::-1] for row in grid) # counter-clockwise rotation
        return grid
    
    seen = {grid}
    array = [grid]
    iter = 0
    while True:
        iter += 1
        grid = cycle(grid)
        
        if grid in seen:
            break
        else:
            seen.add(grid)
            array.append(grid)
    first = array.index(grid)
    cycle_length = iter - first
    grid = array[(10**9-first)%cycle_length+first]
    print(sum(row.count("O") * (len(grid)-i) for i, row in enumerate(grid)))


solveWithTuples("23/input/day14_test.txt", 2)
solveWithTuples("23/input/day14.txt")
solve("23/input/day14_test.txt", 2)
solve("23/input/day14.txt", 2)