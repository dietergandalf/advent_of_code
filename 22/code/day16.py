
def solve(task, file, time):
    with open(file) as f:
        data = f.read().splitlines()
    pipe_speed = {}
    paths = {}
    for line in data:
        line = line[5:].split('; ')
        line[0] = line[0].replace('has flow rate=', '').split()
        line[0][1] = int(line[0][1])
        pipe_speed[line[0][0]] = line[0][1]
        line[1] = line[1].replace(',', '').split()[4:]
        paths[line[0][0]] = line[1]
    
    curr = 'AA'
    opened = []
    pressure_release = 0
    for second in range(time, 0, -1):
        if pipe_speed[curr] == 0 or curr in opened:
            max_speed = 0
            for pipe in paths[curr]:
                if pipe in opened:
                    continue
                if pipe_speed[pipe] >= max_speed:
                    max_speed = pipe_speed[pipe]
                    curr = pipe
            continue
        if curr not in opened:
            opened.append(curr)
            pressure_release += pipe_speed[curr] * (second-1)
            print(curr, pipe_speed[curr], second, pressure_release)


solve(1, '22/input/day16_test.txt', 30)
#solve(1, '22/input/day16.txt')