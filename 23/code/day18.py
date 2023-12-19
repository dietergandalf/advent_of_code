# Day 18 Advent of Code 23

def fillHole(grid):
   # fill the inside of the '#' restricted area with '#'s
   # it is a closed area, so we can just fill it with '#'s
   # by using the flood fill algorithm
   # we start at the top left corner and fill the area
   # until we reach the bottom right corner
   start = (len(grid)//2,len(grid[0])//2)
   end = (len(grid)-1, len(grid[0])-1)
   queue = [start]
   visited = set()
   visited.add(start)
   m = len(grid)
   n = len(grid[0])
   count = 0
   while queue:
      current = queue.pop(0)
      sr,sc = current
      count += 1
      for i in range(-1, 2):
         for j in range(-1, 2):
            if i*j == 0 and sr + i >= 0 and sr + i < m and sc + j >= 0 and sc + j < n and grid[sr+i][sc+j] == "." and (sr+i, sc+j) not in visited:
               queue.append((sr+i, sc+j))
               visited.add((sr+i, sc+j))
               grid[sr+i][sc+j] = "#" 
            
   print(count)
   return grid

def cutGrid(grid):
   minx = 10000000000
   miny = 10000000000
   maxx = 0
   maxy = 0
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         if grid[y][x] == "#":
            if x < minx:
               minx = x
            if x > maxx:
               maxx = x
            if y < miny:
               miny = y
            if y > maxy:
               maxy = y
   grid = grid[miny:maxy+1]
   for i in range(len(grid)):
      grid[i] = grid[i][minx:maxx+1]
   return grid

def solve(file, part=0): # not scalable for part 2
   instr = open(file).read().splitlines()
   instr = [i.split() for i in instr]
   
   DIRECTION = {"R": (0,1), "L": (0,-1), "U": (-1,0), "D": (1,0)}

   width = 1
   height = 1
   start = [0,0]
   for i in instr:
      if i[0] == "R":
         width += int(i[1])
      elif i[0] == "L":
         start[1] += int(i[1])
         width += int(i[1])
      else:
         if i[0] == "D":
            start[0] += int(i[1])
         height += int(i[1])
   grid = [["." for x in range(width)] for y in range(height)]
   
   current = tuple(start)
   for i in instr:
      for _ in range(int(i[1])):
         current = tuple(map(sum, zip(current, DIRECTION[i[0]])))
         grid[current[0]][current[1]] = "#"


   grid = cutGrid(grid)
   grid = fillHole(grid)
   area = 1
   for line in grid:
      print(line)
      area += line.count("#")
   print(area)
   
def solve2(file, part):
   # solve using picks theorem + shoelace formula
   points = [(0,0)]
   dirs = {"R": (0,1), "L": (0,-1), "U": (-1,0), "D": (1,0)}

   b = 0 # number of boundary points


   for line in open(file):
      if part == 0:
         d, n, _ = line.split()
         dr, dc = dirs[d]
         n = int(n)
      else:
         _, _ , x = line.split()
         x = x[2:-1]
         dr, dc = dirs["RDLU"[int(x[-1])]]
         n = int(x[:-1], 16)
      b += n
      r, c = points[-1]
      points.append((r+dr*n, c+dc*n))
   
   A = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % len(points)][1]) for i in range(len(points)))) // 2 # Area
   i = A - b//2 + 1 # number of interior points
   print(i + b) # total area
      

if __name__ == '__main__':
   solve2('C:/Users/malte/programming/advent_of_code/23/input/day18_test.txt', 1)
   print()
   solve2('C:/Users/malte/programming/advent_of_code/23/input/day18.txt', 1)
