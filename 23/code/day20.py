# Day 20 Advent of Code 23

from collections import deque
import math


class Module:
   def __init__(self, name, type, outputs):
      self.name = name
      self.type = type
      self.outputs = outputs
      
      if type == '%':
         self.memory = "off"
      else:
         self.memory = {}
   def __repr__(self) -> str:
      return f"({self.type}{self.name} -> {self.memory} -> {self.outputs})"

def solve(file, part=0):

   modules = {}
   broadcast_targets = []
   commands = open(file).read().strip().split('\n')
   for i,command in enumerate(commands):
      name, targets = command.split(' -> ')
      targets = targets.split(', ')
      if name == "broadcaster":
         broadcast_targets = targets
      else:
         type, name = name[:1],name[1:] 
         commands[i] = command
         modules[name] = (Module(name, type, targets))
      #print(command)
   for name, module in modules.items():
      for output in module.outputs:
         if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "lo"

   if part == 0:
      lows = highs = 0
      BUTTONPRESSES = 1000
      for _ in range(BUTTONPRESSES):
         lows += 1

         # origin target, pulse
         q = deque([("broadcaster", x, "lo") for x in broadcast_targets])

         while q:
            origin, target, pulse = q.popleft()
            if pulse == "lo":
               lows += 1
            else:
               highs += 1
            
            if target not in modules:
               continue
            module = modules[target]
            if module.type == "%":
               if pulse == "hi":
                  continue
               module.memory = "on" if module.memory == "off" else "off"
               outgoing = "hi" if module.memory == "on" else "lo"
               for x in module.outputs:
                  q.append((target, x, outgoing))
            else:
               module.memory[origin] = pulse
               outgoing = "lo" if all([x == "hi" for x in module.memory.values()]) else "hi"
               for x in module.outputs:
                  q.append((target, x, outgoing))
      print(lows* highs)
   else:
      # part 2
      (feed,) = [name for name, module in modules.items() if "rx" in module.outputs]
      # assume feed is a & module -> 4 inputs -> all need to be high
      cycle_lengths = {}
      seen = {name: 0 for name, module in modules.items() if feed in module.outputs}
      
      presses = 0
      while True:
         presses += 1
         q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
         while q:
            origin, target, pulse = q.popleft()
            if target not in modules:
               continue

            module = modules[target]
            
            if module.name == feed and pulse == "hi":
               seen[origin] += 1

               if origin not in cycle_lengths:
                  cycle_lengths[origin] = presses
               else:
                  assert presses == cycle_lengths[origin] * seen[origin]
               
               if all(seen.values()):
                  print(cycle_lengths)
                  print(math.lcm(*cycle_lengths.values()))
                  return

            if module.type == "%":
               if pulse == "hi":
                  continue
               module.memory = "on" if module.memory == "off" else "off"
               outgoing = "hi" if module.memory == "on" else "lo"
               for x in module.outputs:
                  q.append((target, x, outgoing))
            else:
               module.memory[origin] = pulse
               outgoing = "lo" if all([x == "hi" for x in module.memory.values()]) else "hi"
               for x in module.outputs:
                  q.append((target, x, outgoing))


if __name__ == '__main__':
   #solve('C:/Users/malte/programming/advent_of_code/23/input/day20_test.txt', 0)
   solve('C:/Users/malte/programming/advent_of_code/23/input/day20.txt', 1)
