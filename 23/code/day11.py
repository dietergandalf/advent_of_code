def solve(part, file):
    with open(file) as f:
        grid = f.read().splitlines()
    empty_rows = [r for r, row in enumerate(grid) if '#' not in row]
    empty_cols = [c for c in range(len(grid[0])) if '#' not in [row[c] for row in grid]]

    points = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == '#']

    total = 0
    if part == 2:
        scale = 1000000
    else:
        scale = 2

    for i, (r1,c1) in enumerate(points):
        for (r2,c2) in points[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += scale if c in empty_cols else 1
    print(total)

solve(1,'23/input/day11.txt')
solve(2,'23/input/day11.txt')