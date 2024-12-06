# Day 5 Advent of Code 24

from collections import defaultdict

def fix_ordering(incorrect, rulesDict):
    for _, line in enumerate(incorrect):
        while not is_ordered(line, rulesDict):
            for j, num in enumerate(line):
                if num in rulesDict:
                    for r in rulesDict[num]:
                        if r in line and r not in line[:j]:
                            line.remove(r)
                            line.insert(j, r)
    return incorrect

def is_ordered(line: list[int], rulesDict: defaultdict[list]) -> bool:
    for i, num in enumerate(line):
        if num in rulesDict.keys():
            for r in rulesDict[num]:
                if r in line and r not in line[:i]:
                    return False
    return True

def solve(file, part=0):
    with open(file, encoding="utf-8") as f:
        rules, lines = f.read().strip().split('\n\n')
        rules = rules.split('\n')
        lines = lines.split('\n')
        for i, line in enumerate(lines):
            lines[i] = list(map(int, line.split(',')))

    rulesDict = defaultdict(list)
    for rule in rules:
        rule = rule.split("|")
        rulesDict[int(rule[1])].append(int(rule[0]))

    if part == 1:
        incorrect = []
    removeIndicies = set()
    for i, line in enumerate(lines):
        if not is_ordered(line, rulesDict):
            removeIndicies.add(i)

    for i in sorted(removeIndicies, reverse=True):
        if part == 1:
            incorrect.append(lines.pop(i))
        else:
            lines.pop(i)

    if part == 1:
        lines = fix_ordering(incorrect, rulesDict)

    summ = 0
    for line in lines:
        summ += line[len(line)//2]
    print(summ)

if __name__ == '__main__':
    print()
    solve(r'C:\Users\malte\programming\advent_of_code/24/input/day5_test.txt', 1)
    solve(r'C:\Users\malte\programming\advent_of_code/24/input/day5.txt', 1)
