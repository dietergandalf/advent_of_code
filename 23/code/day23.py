# Day 23 Advent of Code 23

if __name__ == '__main__':
   file = 'C:/Users/malte/programming/advent_of_code/23/input/day23_test.txt'
   file = 'C:/Users/malte/programming/advent_of_code/23/input/day23.txt'
   part = 1


grid = open(file).read().strip().split('\n')
start = (int(0), grid[0].index('.'))
end = (len(grid) - 1, grid[-1].index('.'))

points = [start, end]

for r, row in enumerate(grid):
   for c, ch in enumerate(row):
      if ch == '#':
         continue
      neighbors = 0
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
         if 0 <= r + dx < len(grid) and 0 <= c + dy < len(row) and grid[r + dx][c + dy] != '#':
            neighbors += 1
      if neighbors >= 3:
         points.append((r, c))

graph = {pt: {} for pt in points}

if part == 0:
   dirs = {'^': [(-1, 0)], 'v': [(1, 0)], '<': [(0, -1)], '>': [(0, 1)], '.': [(1, 0), (-1, 0), (0, 1), (0, -1)]}
else:
   dirs = {'^': [(1, 0), (-1, 0), (0, 1), (0, -1)], 'v': [(1, 0), (-1, 0), (0, 1), (0, -1)], '<': [(1, 0), (-1, 0), (0, 1), (0, -1)], '>': [(1, 0), (-1, 0), (0, 1), (0, -1)], '.': [(1, 0), (-1, 0), (0, 1), (0, -1)]}
for sr, sc in points:
   stack = [(0, sr, sc)]
   seen = {sr, sc}

   while stack:
      n, r, c = stack.pop()

      if n != 0 and (r, c) in points and (sr, sc) != (r, c):
         graph[(sr, sc)][(r, c)] = n
         continue
      
      for dr, dc in dirs[grid[r][c]]:
         nr = r + dr
         nc = c + dc
         if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in seen:
            stack.append((n + 1, nr, nc))
            seen.add((nr, nc))
print(graph)


seen = set()
def dfs(pt):
   if pt == end:
      return 0
   
   m = -float('inf')

   seen.add(pt)
   for nx in graph[pt]:
      if nx not in seen:
         m = max(m, dfs(nx) + graph[pt][nx])
   seen.remove(pt)

   return m

print(dfs(start))


