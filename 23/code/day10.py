directions = {'N':(0,-1), 'S':(0,1), 'E':(1,0), 'W':(-1,0)}
parts = {'F': ['S', 'E'],'7': ['W', 'S'],'J': ['W', 'N'],'L': ['N', 'E'],'-': ['E', 'W'],'|': ['N', 'S'], '.':[]}


def solve(file):
    with open(file) as f:
        grid = f.readlines()
    
    starting_pos = (0,0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                starting_pos = (x,y)
                break

    end_circle = set()
    S = 'F'
    for part in ['F','7','J','L','-','|']:
        circle = set([starting_pos])
        pos = starting_pos
        curr_part = part
        done = False
        while True:
            if done:
                break
            x, y = pos
            count = 0
            if curr_part == '.' or curr_part == '\n':
                break
            for possible_dir in parts[curr_part]:
                dx, dy = directions[possible_dir]
                if (x+dx, y+dy) not in circle:
                    pos = (x+dx, y+dy)
                    circle.add(pos)
                    curr_part = grid[pos[1]][pos[0]]
                    break
                else:
                    count += 1
                    if count == 2:
                        done = True
                        break
        if len(circle) > len(end_circle):
            correct = False
            for dir in parts[part]:
                dx, dy = directions[dir]
                if (starting_pos[0]+dx, starting_pos[1]+dy) == pos:
                    correct = True
            if correct:
                end_circle = circle
                S = part

    print(S)
    print(len(end_circle) // 2)
    grid[starting_pos[1]] = grid[starting_pos[1]].replace('S', S)
    grid = [''.join(ch if (x,y) in end_circle else '.' for x, ch in enumerate(row)) for y, row in enumerate(grid)]
    outside = set()
    for r,row in enumerate(grid):
        within = False
        up = None
        for c,ch in enumerate(row):
            if ch == '|':
                assert up is None
                within = not within
            elif ch == '-':
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == 'L'
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == '.':
                pass
            else:
                raise RuntimeError("Unexpected character: %s" % ch)
            if not within:
                outside.add((c,r))

    print(len(grid) * len(grid[0]) - len(outside | end_circle))
                

if __name__ == '__main__':
    #solve("23/input/day10_test.txt")
    solve("23/input/day10.txt")
                
