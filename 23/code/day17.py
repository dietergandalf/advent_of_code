# Day 17 Advent of Code 23
from queue import PriorityQueue

def findShortestPath(grid, start, end, max_blocks_per_direction=3, min_blocks_per_direction=0):
   Direction = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1), '': (0, 0)}
   path = PriorityQueue()
   path.put((0, start, '', 0))
   visited = set()
   while path:
      hl, pos, dir, n = path.get()
      dx,dy = Direction[dir]
      if pos == end and n >= min_blocks_per_direction:
         return hl
      if ((pos,dir,n)) in visited:
         continue
      visited.add((pos,dir,n))
      if n < max_blocks_per_direction and dir != '':
         new_pos = (pos[0]+dx, pos[1] + dy)
         if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]):
           path.put((hl + grid[new_pos[0]][new_pos[1]], new_pos, dir, n+1))
      
      if n < min_blocks_per_direction and dir != '':
         continue
      for d in Direction:
         if d == dir or d == '' or Direction[d] == (-dx, -dy):
            continue
         new_pos = (pos[0]+Direction[d][0], pos[1] + Direction[d][1])
         if new_pos[0] < 0 or new_pos[0] >= len(grid) or new_pos[1] < 0 or new_pos[1] >= len(grid[0]):
            continue
         path.put((hl + grid[new_pos[0]][new_pos[1]], new_pos, d, 1))



def solve(file, part=0):
   if part == 0:
      MAX_BLOCKS_PER_DIRECTION = 3
      MIN_BLOCKS_PER_DIRECTION = 0
   else:
      MAX_BLOCKS_PER_DIRECTION = 10
      MIN_BLOCKS_PER_DIRECTION = 4

   grid = open(file).read().splitlines()
   grid = [[int(x) for x in list(line)] for line in grid]
   start = (0, 0)
   end = (len(grid)-1, len(grid[0])-1)
   hl = findShortestPath(grid, start, end, MAX_BLOCKS_PER_DIRECTION, MIN_BLOCKS_PER_DIRECTION)
   print(hl)
   
   
      
if __name__ == '__main__':
   solve('C:/Users/malte/programming/advent_of_code/23/input/day17_test.txt', 1)
   solve('C:/Users/malte/programming/advent_of_code/23/input/day17.txt', 1)
