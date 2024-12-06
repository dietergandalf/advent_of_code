# Day 6 Advent of Code 24

directions = ['^', '>', 'v', '<']

def nextDir(currentDir):
    return directions[(directions.index(currentDir) + 1) % 4]

def solve(file, part=0):
    with(open(file, encoding='utf-8')) as f:
        grid = f.read().strip().split('\n')
        grid = [list(row) for row in grid]
        xMax = len(grid[0])
        yMax = len(grid)
        pos = (0, 0)
        currentDir = '^'
        for i in range(yMax):
            for j in range(xMax):
                if grid[i][j] in directions:
                    pos = (j, i)
                    currentDir = grid[i][j]
                    break

        visited = set()
        while True:
            visited.add(pos)
            if currentDir == '^':
                if pos[1]-1 >= 0 and grid[pos[1]-1][pos[0]] != '#':
                    pos = (pos[0], pos[1] - 1)
                    grid[pos[1]][pos[0]] = 'X'
                elif pos[1]-1 >= 0 and grid[pos[1]-1][pos[0]] == '#':
                    currentDir = nextDir(currentDir)
                else:
                    break
            elif currentDir == '>':
                if pos[0]+1 < xMax and grid[pos[1]][pos[0]+1] != '#':
                    pos = (pos[0] + 1, pos[1])
                    grid[pos[1]][pos[0]] = 'X'
                elif pos[0]+1 < xMax and grid[pos[1]][pos[0]+1] == '#':
                    currentDir = nextDir(currentDir)
                else:
                    break
            elif currentDir == 'v':
                if pos[1]+1 < yMax and grid[pos[1]+1][pos[0]] != '#':
                    pos = (pos[0], pos[1] + 1)
                    grid[pos[1]][pos[0]] = 'X'
                elif pos[1]+1 < yMax and grid[pos[1]+1][pos[0]] == '#':
                    currentDir = nextDir(currentDir)
                else:
                    break
            elif currentDir == '<':
                if pos[0]-1 >= 0 and grid[pos[1]][pos[0]-1] != '#':
                    pos = (pos[0] - 1, pos[1])
                    grid[pos[1]][pos[0]] = 'X'
                elif pos[0]-1 >= 0 and grid[pos[1]][pos[0]-1] == '#':
                    currentDir = nextDir(currentDir)
                else:
                    break
        print(len(visited))

        #for i in range(yMax):
        #    print(grid[i])


if __name__ == '__main__':
    solve(r'C:\Users\malte\programming\advent_of_code/24/input/day6_test.txt', 0)
    solve(r'C:\Users\malte\programming\advent_of_code/24/input/day6.txt', 0)
