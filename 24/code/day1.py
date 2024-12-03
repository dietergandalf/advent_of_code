from typing import List
with open("input/day1.txt") as f:
    lines = f.read().strip()
    while("  " in lines):
        lines = lines.replace("  ", " ")
    lines = lines.split("\n")
    left, right = [], []
    for line in lines:
        left.append(int(line.split(" ")[0]))
        right.append(int(line.split(" ")[1]))

def a(right: List[int], left: List[int]):
    total = 0
    right_sorted = sorted(right)
    left_sorted = sorted(left)
    for i in range(len(left_sorted)):
        total += abs(right_sorted[i] - left_sorted[i])
    print(total)

def b(right: List[int], left: List[int]):
    total = 0
    for i in range(len(left)):
        total += left[i] * right.count(left[i])
    print(total)

a(right, left)
b(right, left)
