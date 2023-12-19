class monkey:
    def __init__(self, items: list[int], operation: list[str], test: int, true: int, false: int):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.operations = 0

    def __str__(self):
        return f"Items: {self.items}, Operation: {self.operation}, Test: {self.test}, True: {self.true}, False: {self.false}, Operations: {self.operations}"

def readinput(file) -> list[monkey]:
    # MonkeyList: 0=Items(list(int)), 1=Operation(list(str)), 2=Test(int), 3=True(int), 4=False(int), 5=Operations(int)
    MonkeyList = []
    with open(file) as f:
        Monkeys = f.read().strip().split("\n\n")
        for monkeyx in Monkeys:

            items = []
            operation = []
            test_stuff = []
            monkeyx = monkeyx.split("\n")
            for i, line in enumerate(monkeyx):
                stuff = line.strip().split(" ")
                if i == 1:
                    for item in stuff:
                        if item == "Starting" or item == "items:":
                            continue
                        item = item.replace(",", "")
                        items.append(int(item))
                elif i == 2:
                    for i in range(len(stuff)):
                        if i > 3:
                            operation.append(stuff[i])
                elif i == 3:
                    test_stuff.append(int(stuff[3]))
                elif i > 3:
                    test_stuff.append(int(stuff[5]))
            stats = monkey(items, operation, test_stuff[0], test_stuff[1], test_stuff[2])
            MonkeyList.append(stats)
    return MonkeyList

def round(MonkeyList: list[monkey], mod: int = 0):
    for monkeyx in MonkeyList:
        while monkeyx.items != []:
            item = monkeyx.items.pop()
            item = calc_worry_lvl(monkeyx, item)
            if mod != 0:
                item %= mod
            else:
                item //= 3
                
            monkeyx.operations += 1
            if check_condition(monkeyx.test, item):
                MonkeyList[monkeyx.true].items.append(item)
            else:
                MonkeyList[monkeyx.false].items.append(item)

def calc_worry_lvl(monkey: monkey, item: int) -> int:
    operator = monkey.operation[0]
    operand = monkey.operation[1]
    if operand == "old":
        operand = item
    else:
        operand = int(operand)
    if operator == "*":
        item *= operand
    elif operator == "+":
        item += operand

    return item

def check_condition(div_by: int, item: int) -> bool:
    return item % div_by == 0

def print_monkey_list(MonkeyList: list[monkey]):
    for monkey in MonkeyList:
        print(f"Monkey {MonkeyList.index(monkey)}:", monkey.items, monkey.operations)
    print()

def get_monkey_buisness(MonkeyList: list[monkey]):
    monkey_buisness = 0
    max_buisness = 0
    second_max_buisness = 0
    for monkey in MonkeyList:
        operations = monkey.operations
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
    for monkeyx in MonkeyList:
        mod *= monkeyx.test
    for _ in range(10_000):
        round(MonkeyList, mod)
    get_monkey_buisness(MonkeyList)
