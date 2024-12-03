# Day 24 Advent of Code 23

import sympy

"""
class Hailstone:
   def __init__(self, data):
      self.start = [data[0], data[1], data[2]]
      self.velocity = (data[3], data[4], data[5])
      # create the line equation, ignore z-axis
      self.slope = self.velocity[1]/self.velocity[0]
      self.line = (self.start[1] - self.slope*self.start[0], self.slope)

   def intersects(self, other: 'Hailstone'):
      LOWER_BOUNDERY = 200000000000000
      UPPER_BOUNDERY = 400000000000000

      if self.slope == other.slope or self.slope == -other.slope:
         return None

      x = (other.line[0] - self.line[0])/(self.line[1] - other.line[1])
      y = self.slope*x + self.line[0]

      print(x, y)

      if (self.velocity[0] < 0 and x > self.start[0]) or (self.velocity[0] > 0 and x < self.start[0]) or (self.velocity[1] < 0 and y > self.start[1]) or (self.velocity[1] > 0 and y < self.start[1]) \
      or (other.velocity[0] < 0 and x > other.start[0]) or (other.velocity[0] > 0 and x < other.start[0]) or (other.velocity[1] < 0 and y > other.start[1]) or (other.velocity[1] > 0 and y < other.start[1]):
         return None

      if LOWER_BOUNDERY <= x <= UPPER_BOUNDERY and LOWER_BOUNDERY <= y <= UPPER_BOUNDERY:
         return (x, y)

      return None
   
   def __repr__(self) -> str:
      return f"{self.line}"

"""

def solve(file, part=0):
   #hailstones = [Hailstone(data) for data in [list(map(int, line.replace(" @", ",").split(", "))) for line in open(file)]]
   hailstones = [tuple(map(int, line.replace(" @", ",").split(", "))) for line in open(file)]

   if part == 0:
      LOWER_BOUNDERY = 200000000000000
      UPPER_BOUNDERY = 400000000000000
      total = 0

      for i, hailstone in enumerate(hailstones):
         for hailstone2 in hailstones[i+1:]:
            px, py = sympy.symbols('px py')
            answers = sympy.solve([vy * (px - sx) - vx * (py - sy) for sx, sy, _, vx, vy, _ in [hailstone, hailstone2]], [px, py])
            if answers == []:
               continue
            x, y = answers[px], answers[py]
            if LOWER_BOUNDERY <= x <= UPPER_BOUNDERY and LOWER_BOUNDERY <= y <= UPPER_BOUNDERY:
               if all((x - sx) * vx >= 0 and (y - sy) * vy >= 0 for sx, sy, _, vx, vy, _ in [hailstone, hailstone2]):
                  total += 1
      return total

   xr, yr, zr, vxr, vyr, vzr = sympy.symbols('xr yr zr vxr vyr vzr')
   equations = []

   for sx, sy, sz, vx, vy, vz in hailstones:
      equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
      equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
   
   answers = sympy.solve(equations)
   return answers[0][xr] + answers[0][yr] + answers[0][zr]

   """
   intersections = []
   for i in range(len(hailstones)):
      for j in range(i+1, len(hailstones)):
         intersection = hailstones[i].intersects(hailstones[j])
         if intersection is not None:
            intersections.append(intersection)

   print(len(intersections))
   """
      

if __name__ == '__main__':
   print(solve('C:/Users/malte/programming/advent_of_code/23/input/day24_test.txt', 1))
   print(solve('C:/Users/malte/programming/advent_of_code/23/input/day24.txt', 1))
