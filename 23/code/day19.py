# Day 19 Advent of Code 23

class Part:
   def __init__(self, x: int, m: int, a: int, s: int):
      self.x = x
      self.m = m
      self.a = a
      self.s = s
   
   def getSum(self):
      return self.x + self.m + self.a + self.s

   def __repr__(self):
      return f"(x={self.x} m={self.m} a={self.a} s={self.s})"

class Rule:
   def __init__(self, operator: str, check_type: str, check_val: int, accept_rule: str, else_rule: str):
      self.check_type = check_type
      self.operator = operator
      self.check_val = check_val
      self.accept_rule = accept_rule
      self.else_rule = else_rule
   
   def check(self, part):
      if self.check_type == 'x':
         if self.operator == '>':
            return part.x > self.check_val
         elif self.operator == '<':
            return part.x < self.check_val
         elif self.operator == '=':
            return part.x == self.check_val
      elif self.check_type == 'm':
         if self.operator == '>':
            return part.m > self.check_val
         elif self.operator == '<':
            return part.m < self.check_val
         elif self.operator == '=':
            return part.m == self.check_val
      elif self.check_type == 'a':
         if self.operator == '>':
            return part.a > self.check_val
         elif self.operator == '<':
            return part.a < self.check_val
         elif self.operator == '=':
            return part.a == self.check_val
      elif self.check_type == 's':
         if self.operator == '>':
            return part.s > self.check_val
         elif self.operator == '<':
            return part.s < self.check_val
         elif self.operator == '=':
            return part.s == self.check_val
      else:
         print("Error: Invalid check type")
         return False
   
   def __repr__(self):
      return f"{self.check_type} {self.operator} {self.check_val} -> {self.accept_rule} else {self.else_rule}"

class Workflow:
   def __init__(self, name: str, rules: list[Rule]):
      self.name = name
      self.rules = rules

   def applyRule(self, part):
      for rule in self.rules:
         if rule.check(part):
            return rule.accept_rule
      return rule.else_rule

   def __repr__(self):
      return f"{self.name}: {self.rules}"


def count(ranges, name, workflowDict): # only used in part 2
   if name =="R":
      return 0
   if name == "A":
      product = 1
      for lo, hi in ranges.values():
         product *= hi - lo + 1
      return product
   
   workflow = workflowDict.get(name)
   
   total = 0

   for rule in workflow.rules:
      lo, hi = ranges[rule.check_type]
      if rule.operator == "<":
         T = (lo, rule.check_val-1)
         F = (rule.check_val, hi)
      else:
         T = (rule.check_val+1, hi)
         F = (lo, rule.check_val)
      if T[0] <= T[1]:
         copy = dict(ranges)
         copy[rule.check_type] = T
         total += count(copy, rule.accept_rule, workflowDict)
      if F[0] <= F[1]:
         ranges = dict(ranges)
         ranges[rule.check_type] = F
      else:
         break
   else:
      total += count(ranges, workflow.rules[-1].else_rule, workflowDict)
   return total

def solve(file, part=0):
   workflows, parts = open(file).read().strip().split('\n\n')
   workflows = workflows.split('\n')
   parts = parts.split('\n')
   workflowDict = {}
   for i in range(len(parts)):
      part = parts[i].replace("{","").replace("}","").split(',')
      part = [int(x[2:]) for x in part]
      parts[i] = Part(part[0], part[1], part[2], part[3])
   for i in range(len(workflows)):
      name, rules = workflows[i].split('{')
      rules = rules.replace("}", "").split(',')
      rules = [x.split(':') for x in rules]
      Regeln = []
      for j, rule in enumerate(rules):
         else_rule = rules[-1][0]
         if j < len(rules)-1:
            accept_rule = rule[-1]
         for x in rule[:-1]:
            category = x[:1]
            operator = x[1:2]
            value = int(x[2:])
            Regeln.append(Rule(operator, category, value, accept_rule, else_rule))
      
      workflowDict[name] = Workflow(name, Regeln)

   ENDSTATE = {'A', 'R'}
   summ = []
   if part == 0:
      for part in parts:
         current_workflow: Workflow = workflowDict.get('in')
         while True:
            next = current_workflow.applyRule(part)
            if next in ENDSTATE:
               if next == 'A':
                  summ.append(part.getSum())
                  break
               else:
                  break
            current_workflow = workflowDict.get(next)
   else:
      print(count({key: (1, 4000) for key in "xmas"}, "in", workflowDict))
   #print(sum(summ))
   


if __name__ == '__main__':
   solve('C:/Users/malte/programming/advent_of_code/23/input/day19_test.txt', 1)
   solve('C:/Users/malte/programming/advent_of_code/23/input/day19.txt', 1)
