with open("input/day1.txt") as f:
    data = f.read().splitlines()

class indexNr:
    def __init__(self, index: int, number: int):
        self.index = index
        self.number = number

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for line in data:
    ints: list[indexNr] = []

    for i in range(len(line)):
        if line[i].isdigit():
            ints.append(indexNr(i, int(line[i])))
        for num in numbers:
            if line[i:i+len(num)] == num:
                ints.append(indexNr(i, numbers.index(num)))
    ints.sort(key=lambda x: x.index)
    sum += ints[0].number * 10 + ints[-1].number
print(sum)
