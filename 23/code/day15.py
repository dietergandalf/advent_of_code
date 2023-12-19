def hash(str):
    val = 0
    for c in str:
        val = ((val + ord(c)) * 17) % 256
    return val

def solve(file, part= 0):
    instructions = open(file).read().strip().split(",")
    result = 0
    boxes = [[] for _ in range(256)]
    focal_lengths = {}

    for instr in instructions:
        result += hash(instr)
        if part == 0:
            continue
        if "-" in instr:
            label = instr[:-1]
            index = hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = instr.split("=")
            length = int(length)

            index = hash(label)
            if label not in boxes[index]:
                boxes[index].append(label)

            focal_lengths[label] = length
    if part == 0:
        print(result)
        return
    
    total = 0
    for box_nr, box in enumerate(boxes, 1):
        for lens_slot, label in enumerate(box, 1):
            total += box_nr * lens_slot * focal_lengths[label]
    print(total)

solve("23/input/day15_test.txt", 1)
solve("23/input/day15.txt", 1)
