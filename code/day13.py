
from functools import cmp_to_key


def compare(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]
    if isinstance(a, int) and isinstance(b, list):
        a = [a]
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        if a == b:
            return 0
        return -1
    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            x = compare(a[i], b[i])
            if x != 0:
                return x
            i += 1
        
        if i == len(a):
            if len(a) == len(b):
                return 0
            return 1
        return -1

with open("input/day13.txt", "r") as f:
    packages = f.read().strip().split("\n\n")

count = 0
packets = []
for index, package in enumerate(packages):
    line1, line2 = package.split("\n")
    array1 = eval(line1)
    array2 = eval(line2)
    packets.append(array1)
    packets.append(array2)
    if compare(array1, array2) == 1:
        count += (index + 1)
print(count)


packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
start_index = packets.index([[2]]) + 1
end_index = packets.index([[6]]) + 1
print(start_index, end_index, start_index * end_index)