# Day 22 Advent of Code 23

from collections import deque


def solve(file, part=0):
   bricks = [list(map(int, line.replace('~', ',').split(','))) for line in open(file)]
   """
   data = open(file).read().strip().split('\n')
   bricks = []
   for line in data:
      x1,y1,z1 = list(map(int, line.split('~')[0].split(',')))
      x2,y2,z2 = list(map(int, line.split('~')[1].split(',')))
      bricks.append([x1,y1,z1,x2,y2,z2])
   """
   
   bricks.sort(key=lambda z: z[2])

   def overlaps(a, b):
      return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])
   

   for index, brick in enumerate(bricks):
      max_z = 1
      for check in bricks[:index]:
         if overlaps(brick, check):
            max_z = max(check[5] + 1, max_z)
         brick[5] += max_z - brick[2]
         brick[2] = max_z

   bricks.sort(key=lambda z: z[2])
   
   k_supports_v = {i: set() for i in range(len(bricks))}
   v_supports_k = {i: set() for i in range(len(bricks))}
   
   for j, upper in enumerate(bricks):
      for i, lower in enumerate(bricks[:j]):
         if overlaps(lower, upper) and lower[5] + 1 == upper[2]:
            k_supports_v[i].add(j)
            v_supports_k[j].add(i)
   
   total = 0
   for i in range(len(bricks)):
      if part == 1:
         q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
         falling = set(q)
         falling.add(i)
         while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling:
               if v_supports_k[k] <= falling:
                  q.append(k)
                  falling.add(k)
         total += len(falling) - 1

      if part == 0 and all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
         total += 1
   print(total)

if __name__ == '__main__':
   solve('C:/Users/malte/programming/advent_of_code/23/input/day22_test.txt', 1)
   solve('C:/Users/malte/programming/advent_of_code/23/input/day22.txt', 1)
