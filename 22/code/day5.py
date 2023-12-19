# move count crates from stack1 to stack2
def move(count: int, stack1: int, stack2:int):
    global stacks
    for _ in range(count):
        # move crate from stack1 to stack2
        stacks[stack2-1].append(stacks[stack1-1].pop())

# move crates from stack1 to stack2 but keep the same order
def move2(count: int, stack1: int, stack2:int):
    global stacks
    tmp_stack = []
    for _ in range(count):
        # move crate from stack1 to stack2
        tmp_stack.append(stacks[stack1-1].pop())
    while tmp_stack != []:
        stacks[stack2-1].append(tmp_stack.pop())


if __name__ == "__main__":
    stacks = [[] for _ in range(9)]
    with open("input/day5.txt", "r") as f:
        drawing, procedure = f.read().split("\n\n")
        # parse drawing
        for line in drawing.splitlines():
            length = len(line)
            index = 0
            for i in range(1, length, 4):
                if line[i] != " " and line[i] not in "0123456789":
                    stacks[index].append(line[i])
                index += 1
        for stack in stacks:
            stack.reverse()
            
        # parse procedure
        for line in procedure.splitlines():
            text = line.split()
            count = int(text[1])
            stack1 = int(text[3])
            stack2 = int(text[5])
            #move(count, stack1, stack2)
            move2(count, stack1, stack2)
    
    # get the top crate of each stack and join them to a string
    for stack in stacks:
        print("".join(stack[-1]), end="")