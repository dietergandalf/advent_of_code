with open("input/day3.txt") as f:
    grid = f.read().splitlines()

def a():
    cs = set()
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

    ns = []

    for r, c in cs:
        s = ""
        while c < len(grid[r]) and grid[r][c].isdigit():
            s += grid[r][c]
            c += 1
        ns.append(int(s))

    print(sum(ns))

def b():
    sum = 0
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch != "*":
                continue
            
            cs = set()

            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

            if len(cs) != 2:
                continue

            ns = []

            for ri, ci in cs:
                s = ""
                while ci < len(grid[ri]) and grid[ri][ci].isdigit():
                    s += grid[ri][ci]
                    ci += 1
                ns.append(int(s))
            
            sum += ns[0] * ns[1]

    print(sum)

def main():
    a()
    b()

if __name__ == "__main__":
    main()