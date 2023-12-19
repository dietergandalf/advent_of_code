
with open("input/day1.txt", "r") as f:
    data = f.read()
    data_per_elf = data.split("\n\n")
    elves = []
    for i, data in enumerate(data_per_elf):
      elves.append([int(x) for x in data.split("\n")])
    sums = sorted([sum(elf) for elf in elves])
    print(sums[-3:])
    print(sums[-1]+sums[-2]+sums[-3])