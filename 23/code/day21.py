# Day 21 Advent of Code 23
from collections import deque

def solveA(file, part=0, steps=64):
   grid = open(file).read().strip().split('\n')
   DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
   cache = {}

   size = len(grid)

   start = None
   for y in range(size):
      for x in range(size):
         if grid[y][x] == 'S':
            start = (x,y)
   different_spaces = set()
   different_spaces.add(start)
   for _ in range(steps):
      new_different_spaces = set()
      for x,y in different_spaces:
         next_poses = set()
         if (x,y) in cache:
            next_poses = cache[(x,y)]
            new_different_spaces.update(next_poses)
            continue
         for dx,dy in DIRS:
            new_x, new_y = x+dx, y+dy
            if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid) or grid[new_y][new_x] == '#':
               continue
            new_different_spaces.add((new_x, new_y))
            next_poses.add((new_x, new_y))
         cache[(x,y)] = next_poses
            
      different_spaces = new_different_spaces
     
   print(len(different_spaces))

def solve(file, part=0, steps = 64):
   grid = open(file).read().splitlines()

   sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == 'S')

   size = len(grid)
   if part == 1:
      assert len(grid) == len(grid[0])  # grid is square
      assert sr == sc == len(grid) // 2  # start is in the middle
      assert steps % size == size // 2  # steps is a multiple of grid size
      

   def fill(sr, sc, ss):
      ans = set()
      seen = {(sr, sc)}
      q = deque([(sr, sc, ss)])
      while q:
         r, c, s = q.popleft()
         
         if s % 2 == 0:
            ans.add((r, c))
         if s == 0:
            continue
         for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in seen:
               seen.add((nr, nc))
               q.append((nr, nc, s - 1))
      return(len(ans))
   

   if part == 0:
      print(fill(sr, sc, steps))
      return
   grid_width = steps // size - 1

   odd = (grid_width // 2 * 2 + 1) ** 2
   even = ((grid_width + 1) // 2 * 2) ** 2

   odd_points = fill(sr, sc, size * 2 + 1)
   even_points = fill(sr, sc, size * 2)

   corner_t = fill(size - 1, sc, size - 1)
   corner_r = fill(sr, 0, size - 1)
   corner_b = fill(0, sc, size - 1)
   corner_l = fill(sr, size - 1, size - 1)

   small_tr = fill(size - 1, 0, size // 2 - 1)
   small_tl = fill(size - 1, size - 1, size // 2 - 1)
   small_br = fill(0, 0, size // 2 - 1)
   small_bl = fill(0, size - 1, size // 2 - 1)

   large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
   large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
   large_br = fill(0, 0, size * 3 // 2 - 1)
   large_bl = fill(0, size - 1, size * 3 // 2 - 1)

   print(
      odd * odd_points + 
      even * even_points + 
      corner_t + corner_r + corner_b + corner_l + 
      (grid_width + 1) * (small_tr + small_tl + small_br + small_bl) + 
      (grid_width) * (large_tr + large_tl + large_br + large_bl)
   )


if __name__ == '__main__':
   #solve('C:/Users/malte/programming/advent_of_code/23/input/day21_test.txt', 0)
   #solve('C:/Users/malte/programming/advent_of_code/23/input/day21.txt', 0)
   solve('C:/Users/malte/programming/advent_of_code/23/input/day21.txt', 1, 26501365)