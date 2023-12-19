from math import gcd

select = {'L' : 0, 'R' : 1}

def solve(part, file):
    with open(file) as f:
        start, _, *data = f.read().splitlines()
    instructions = {}
    for i, line in enumerate(data):
        key, value = line.split(' = ')
        instructions[key] = value[1:-1].split(', ')
    
    curr = []
    index = 0
    steps = 0
    cycle = []

    if part == 1:
        curr.append('AAA')
    else:
        curr = [key for key in instructions.keys() if key[-1] == 'A']

    while True:
        steps += 1
        if not curr:
            break
        for i, node in enumerate(curr):
            curr[i] = instructions[node][select[start[index]]]
        index = (index + 1) % len(start)
        for node in curr:
            if node[-1] == 'Z':
                cycle.append(steps)
                curr.remove(node)
    
    steps = 1
    for num in cycle:
        steps = steps * num // gcd(steps, num)
    print(steps)


solve(1, "23/input/day8.txt")
solve(2, "23/input/day8.txt")