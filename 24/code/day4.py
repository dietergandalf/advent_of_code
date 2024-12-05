# Day 4 Advent of Code 24

def checkXMAS(grid, i, j):
   """check if the current cell is a start point for XMAS
      check if any direction is an M, if so, Check for A and S is the next cells in that direction
      skip directions if the grid is out of bounds
      """
   count = 0
   # check upwards
   if i - 3 >= 0: #straight up
      if grid[i-1][j] == "M" and grid[i-2][j] == "A" and grid[i-3][j] == "S":
         count += 1
      if j - 3 >= 0 and grid[i-1][j-1] == "M" and grid[i-2][j-2] == "A" and grid[i-3][j-3] == "S": #up left
         count += 1
      if j + 3 < len(grid[0]) and grid[i-1][j+1] == "M" and grid[i-2][j+2] == "A" and grid[i-3][j+3] == "S": #up right
         count += 1
   # check downwards
   if i + 3 < len(grid):
      if grid[i+1][j] == "M" and grid[i+2][j] == "A" and grid[i+3][j] == "S": #straight down
         count += 1
      if j - 3 >= 0 and grid[i+1][j-1] == "M" and grid[i+2][j-2] == "A" and grid[i+3][j-3] == "S": #down left
         count += 1
      if j + 3 <= len(grid[0])-1 and grid[i+1][j+1] == "M" and grid[i+2][j+2] == "A" and grid[i+3][j+3] == "S": #down right
         count += 1
   # check left
   if j - 3 >= 0:
      if grid[i][j-1] == "M" and grid[i][j-2] == "A" and grid[i][j-3] == "S":
         count += 1
   # check right
   if j + 3 < len(grid[0]):
      if grid[i][j+1] == "M" and grid[i][j+2] == "A" and grid[i][j+3] == "S":
         count += 1
   return count

def checkMAS(grid, i, j):
   count = 0
   if i - 1 < 0 or j - 1 < 0 or i + 1 >= len(grid) or j + 1 >= len(grid[0]):
      return count
   upLeftCheck = False
   if grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S" or grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M":
      upLeftCheck = True
   if upLeftCheck and (grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" or grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M"):
      count += 1
   return count

def solve(file, part=0):
   with open(file) as f:
      grid = f.read().splitlines()
   summ = 0
   try:
      for i in range(len(grid)):
         for j in range(len(grid[0])):
            if part == 0:
               if grid[i][j] == "X":
                  summ += checkXMAS(grid, i, j)
            else:
               if grid[i][j] == "A":
                  summ += checkMAS(grid, i, j)
   except IndexError:
      print("Index out of bounds", i, j)
      pass
   print(summ)


if __name__ == '__main__':
   solve(r'C:\Users\malte\programming\advent_of_code/24/input/day4_test.txt', 1)
   solve(r'C:\Users\malte\programming\advent_of_code/24/input/day4.txt', 1)
