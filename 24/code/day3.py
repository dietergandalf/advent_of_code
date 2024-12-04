# Day 3 Advent of Code 24

def solve(file, part=0):
   if part == 0:
      with open(file, encoding="utf-8") as f:
         lines = f.read().strip().split("mul(")
         for i in range(len(lines)):
            lines[i] = lines[i].split(")")[0]
            lines[i] = lines[i].split(",")
         for i in range(len(lines)-1, -1, -1):
            print(lines[i], len(lines[i]))
            if len(lines[i]) != 2:
               print("popped")
               lines.pop(i)
               continue
            for j,x in enumerate(lines[i]):
               try:
                  lines[i][j] = int(x)
               except ValueError:
                  print("popped")
                  lines.pop(i)
         print(lines)
         summ = 0
         for multiplication in lines:
            summ += multiplication[0] * multiplication[1]
         print(summ)

   else:
      with open(file, encoding="utf-8") as f:
         lines = f.read().strip()
         summ = 0
         lines = lines.split("do()")
         calculations = []
         for i, line in enumerate(lines):
            lines[i] = line.split("don't()")[0]
         for i, line in enumerate(lines):
            lines[i] = line.split("mul(")
            lines[i] = [x.split(")") for x in lines[i]]
            for j, x in enumerate(lines[i]):
               for y in x:
                  calculations.append(y)
                  calculations[-1] = calculations[-1].split(",")
         for i in range(len(calculations)-1, -1, -1):
            if len(calculations[i]) != 2:
               calculations.pop(i)
               continue
            for j in range(len(calculations[i])-1, -1, -1):
               try:
                  calculations[i][j] = int(calculations[i][j])
               except ValueError:
                  calculations.pop(i)
               
         for calculation in calculations:
            summ += calculation[0] * calculation[1]
         print(summ)
      


if __name__ == '__main__':
   solve('C:\\Users\\malte\\programming\\advent_of_code/24/input/day3_test.txt', 1)
   solve('C:\\Users\\malte\\programming\\advent_of_code/24/input/day3.txt', 1)
