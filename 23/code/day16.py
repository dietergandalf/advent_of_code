# Day 16 Advent of Code 23

def getEnergized(grid, pos, dir):
   energized = set()
   beams = []
   DIRS = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
   beams.append((pos, dir))
   energized.add(pos)
   checked = set()
   while beams != []:
      beam = beams.pop()
      if beam in checked:
         continue
      checked.add(beam)
      pos, dir = beam
      direction = DIRS[dir]
      if pos not in energized:
         energized.add(pos)
      if pos[0] + direction[0] >= len(grid) or pos[0] + direction[0] < 0 or pos[1] + direction[1] >= len(grid[0]) or pos[1] + direction[1] < 0:
         continue
      check = (pos[0] + direction[0],pos[1] + direction[1])
      if grid[check[0]][check[1]] == '.':
         beams.append(((check[0],check[1]), dir))
      elif grid[check[0]][check[1]] == '/':
         if dir == 'R':
            beams.append(((check[0],check[1]), 'U'))
         elif dir == 'L':
            beams.append(((check[0],check[1]), 'D'))
         elif dir == 'U':
            beams.append(((check[0],check[1]), 'R'))
         elif dir == 'D':
            beams.append(((check[0],check[1]), 'L'))
      elif grid[check[0]][check[1]] == '\\':
         if dir == 'R':
            beams.append(((check[0],check[1]), 'D'))
         elif dir == 'L':
            beams.append(((check[0],check[1]), 'U'))
         elif dir == 'U':
            beams.append(((check[0],check[1]), 'L'))
         elif dir == 'D':
            beams.append(((check[0],check[1]), 'R'))
      elif grid[check[0]][check[1]] == '-':
         if dir in 'RL':
            beams.append(((check[0],check[1]), dir))
         elif dir in 'UD':
            beams.append(((check[0],check[1]), 'R'))
            beams.append(((check[0],check[1]), 'L'))
      elif grid[check[0]][check[1]] == '|':
         if dir in 'UD':
            beams.append(((check[0],check[1]), dir))
         else:
            beams.append(((check[0],check[1]), 'U'))
            beams.append(((check[0],check[1]), 'D'))
      else:
         beams.append((pos, dir))

   return (len(energized))

def solve(file, part=0):
   grid = open(file).read().splitlines()
   grid = [list(line) for line in grid]
   if part == 0:
      print(getEnergized(grid, (0, 0), 'R'))
   else:
      values = []
      for r in range(len(grid)):
         pos = (r, 0)
         dir = 'R'
         values.append(getEnergized(grid, pos, dir))
         pos = (r, len(grid[0])-1)
         dir = 'L'
         values.append(getEnergized(grid, pos, dir))
      for c in range(len(grid[0])):
         pos = (0, c)
         dir = 'D'
         values.append(getEnergized(grid, pos, dir))
         pos = (len(grid)-1, c)
         dir = 'U'
         values.append(getEnergized(grid, pos, dir))
      print(max(values))
      
   
   

if __name__ == '__main__':
   solve('C:/Users/malte/programming/advent_of_code/23/input/day16_test.txt', 1)
   solve('C:/Users/malte/programming/advent_of_code/23/input/day16.txt', 1)
