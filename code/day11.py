def readinput(file):
    # MonkeyList: 0=Items(list(int)), 1=Operation(list(str)), 2=Test(int), 3=True(int), 4=False(int)
    MonkeyList = []
    with open(file) as f:
        Monkeys = f.read().strip().split("\n\n")
        for monkey in Monkeys:
            stats = []
            monkey = monkey.split("\n")
            for i, line in enumerate(monkey):
                stuff = line.strip().split(" ")
                items = []
                operation = []
                if i == 1:
                    for item in stuff:
                        if item == "Starting" or item == "items:":
                            continue
                        item = item.replace(",", "")
                        items.append(int(item))
                    stats.append(items)
                elif i == 2:
                    for i in range(len(stuff)):
                        if i > 3:
                            operation.append(stuff[i])
                    stats.append(operation)
                elif i == 3:
                    stats.append(int(stuff[3]))
                elif i == 4 or i == 5:
                    stats.append(int(stuff[5]))
            stats.append(0)
            MonkeyList.append(stats)
    return MonkeyList

def round(MonkeyList, mod: int = 0):
    for monkey in MonkeyList:
        while monkey[0] != []:
            item = monkey[0].pop()
            item = calc_worry_lvl(monkey, item)
            if mod != 0:
                item %= mod
            else:
                item //= 3
                
            monkey[5] += 1
            if check_condition(monkey[2], item):
                MonkeyList[monkey[3]][0].append(item)
            else:
                MonkeyList[monkey[4]][0].append(item)

def calc_worry_lvl(monkey, item: int) -> int:
    operator = monkey[1][0]
    operand = monkey[1][1]
    if operand == "old":
        operand = item
    else:
        operand = int(operand)
    if operator == "*":
        item *= operand
    elif operator == "+":
        item += operand

    return item

def check_condition(div_by, item: int) -> bool:
    return item % div_by == 0

def print_monkey_list(MonkeyList):
    for monkey in MonkeyList:
        print(f"Monkey {MonkeyList.index(monkey)}:", monkey[0], monkey[5])
    print()

def get_monkey_buisness(MonkeyList):
    monkey_buisness = 0
    max_buisness = 0
    second_max_buisness = 0
    for monkey in MonkeyList:
        operations = monkey[5]
        if operations > max_buisness:
            second_max_buisness = max_buisness
            max_buisness = operations
        elif operations > second_max_buisness:
            second_max_buisness = operations
    monkey_buisness = max_buisness * second_max_buisness
    print(monkey_buisness)


if __name__ == "__main__":
    MonkeyList = readinput("input/day11.txt")
    
    # Part 1
    for _ in range(20):
        round(MonkeyList)
    get_monkey_buisness(MonkeyList)
    
    # Part 2
    mod = 1
    for monkey in MonkeyList:
        mod *= monkey[2]
    for _ in range(10_000):
        round(MonkeyList, mod)
    get_monkey_buisness(MonkeyList)    
