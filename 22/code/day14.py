def a():
    with open("input/day14.txt") as f:
        lines = f.read().strip().splitlines()


    def print_point(point):
        if point == 0:
            print(".", end="")
        elif point == 1:
            print("#", end="")
        if point == 2:
            print("+", end="")
        if point == -1:
            print("o", end="")

    def print_map(grid):
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                point = grid[x][y]
                print_point(point)
            print()
            print()

    def fill_line(grid, start, end):
        if start[0] == end[0]:
            if start[1] > end[1]:
                for y in range(end[1], start[1] + 1):
                    grid[start[0]][y] = 1
            else:
                for y in range(start[1], end[1] + 1):
                    grid[start[0]][y] = 1
        else:
            if start[0] > end[0]:
                for x in range(end[0], start[0] + 1):
                    grid[x][start[1]] = 1
            else:
                for x in range(start[0], end[0] + 1):
                    grid[x][start[1]] = 1

    def sand_physics(grid, sand):
        while True:
            if sand[1] == maxy:
                return None
                
            if grid[sand[0]][sand[1] + 1] == 0:
                sand = (sand[0], sand[1] + 1)
            elif grid[sand[0] - 1][sand[1] + 1] == 0:
                sand = (sand[0] - 1, sand[1] + 1)
            elif grid[sand[0] + 1][sand[1] + 1] == 0:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                grid[sand[0]][sand[1]] = -1
                return sand


    minx = 500 # 494
    maxx = 0 # 503
    miny = 0
    maxy = 0 # 9
    sand_start = (500, 0)

    lines_arr = []
    for line in lines:
        line_arr = []
        line = line.split(" -> ")
        for linex in line:
            x = int(linex[:linex.index(",")])
            y = int(linex[linex.index(",")+1:])
            coords = (x, y)
            line_arr.append(coords)
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        lines_arr.append(line_arr)

    grid = [[0] * (maxy + 1) for _ in range(maxx + 1)]
    for line in lines_arr:
        for i in range(len(line) - 1):
            start = line[i]
            end = line[i+1]
            fill_line(grid, start, end)
    grid[sand_start[0]][sand_start[1]] = 2

    sand_falling = True
    count = 0
    while sand_falling:
        sand = (sand_start[0], sand_start[1] + 1)
        sand = sand_physics(grid, sand)
        if sand:
            count += 1
        else:
            sand_falling = False
    #print_map(grid)
    print(count)


def b():
    with open("input/day14.txt") as f:
        lines = f.read().strip().splitlines()


    def print_point(point):
        if point == 0:
            print(".", end="")
        elif point == 1:
            print("#", end="")
        if point == 2:
            print("+", end="")
        if point == -1:
            print("o", end="")

    def print_map(grid):
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                point = grid[x][y]
                print_point(point)
            print()
            print()

    def fill_line(grid, start, end):
        if start[0] == end[0]:
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                grid[start[0]][y] = 1
        else:
            for x in range(min(start[0], end[0]), max(start[0],end[0]) + 1):
                grid[x][start[1]] = 1

    def sand_physics(grid, sand):
        while True:
                
            if grid[sand[0]][sand[1] + 1] == 0:
                sand = (sand[0], sand[1] + 1)
            elif grid[sand[0] - 1][sand[1] + 1] == 0:
                sand = (sand[0] - 1, sand[1] + 1)
            elif grid[sand[0] + 1][sand[1] + 1] == 0:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                grid[sand[0]][sand[1]] = -1
                if sand[1] == sand_start[1] and sand[0] == sand_start[0]:
                    return None
                return sand


    minx = 500 # 494
    maxx = 0 # 503
    miny = 0
    maxy = 0 # 9
    sand_start = (500, 0)

    lines_arr = []
    for line in lines:
        line_arr = []
        line = line.split(" -> ")
        for linex in line:
            x = int(linex[:linex.index(",")])
            y = int(linex[linex.index(",")+1:])
            coords = (x, y)
            line_arr.append(coords)
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        lines_arr.append(line_arr)

    maxy += 2
    maxx = 500 + maxy - miny + 1
    minx = 500 - maxy + miny - 1


    grid = [[0] * (maxy + 1) for _ in range(maxx + 1)]
    for line in lines_arr:
        for i in range(len(line) - 1):
            start = line[i]
            end = line[i+1]
            fill_line(grid, start, end)
    grid[sand_start[0]][sand_start[1]] = 2

    for x in range(minx, maxx + 1):
        grid[x][maxy] = 1

    sand_falling = True
    count = 0
    while sand_falling:
        sand = (sand_start[0], sand_start[1])
        sand = sand_physics(grid, sand)
        count += 1
        if not sand:
            sand_falling = False
    #print_map(grid)
    print(count)


def main():
    a()
    b()

if __name__ == "__main__":
    main()

