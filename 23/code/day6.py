s = "input/day6.txt"
t = "input/day6_test.txt"

def a(file):
    with open(file) as f:
        data = f.read().split("\n")
    for i, line in enumerate(data):
        while "  " in line:
            line = line.replace("  ", " ")
        line = list(map(int, line.split(" ")[1:]))
        data[i] = line

    sum = 1
    for i, race_length in enumerate(data[0]):
        winning = []
        for speed in range(1, race_length):
            if (race_length - speed) * speed > data[1][i]:
                winning.append(speed)
        sum *= len(winning)

    print(sum)

def b(file):
    with open(file) as f:
        data = f.read().split("\n")
    for i, line in enumerate(data):
        while " " in line:
            line = line.replace(" ", "")
        line = list(map(int,(line.split(":")[1:])))
        data[i] = line[0]
    
    # find lowest winning speed and highest winning speed
    lowest, highest  = data[0], 0
    for i in range(1, data[0]):
        if (data[0] - i) * i > data[1]:
            lowest = i
            break
    for i in range(data[0], 1, -1):
        if (data[0] - i) * i > data[1]:
            highest = i
            break
    print(highest-lowest + 1)



if __name__ == "__main__":
    a(s)
    print("\n")
    b(s)