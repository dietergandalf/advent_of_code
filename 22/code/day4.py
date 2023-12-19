
def count_full_overlaps():
    counter = 0
    with open("input/day4.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            elf1_range, elf2_range = line.split(",")
            elf1_low, elf1_high = int(elf1_range.split("-")[0]), int(elf1_range.split("-")[1])
            elf2_low, elf2_high = int(elf2_range.split("-")[0]), int(elf2_range.split("-")[1])
            print(elf1_low, elf1_high, elf2_low, elf2_high)
            # if elf2_range in elf1_range or vice versa:
            if elf1_low <= elf2_low and elf2_high <= elf1_high or elf2_low <= elf1_low and elf1_high <= elf2_high:
                counter += 1
    print(counter)
    
def count_overlaps():
    counter = 0
    with open("input/day4.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            elf1_range, elf2_range = line.split(",")
            elf1_low, elf1_high = int(elf1_range.split("-")[0]), int(elf1_range.split("-")[1])
            elf2_low, elf2_high = int(elf2_range.split("-")[0]), int(elf2_range.split("-")[1])
            if elf1_low <= elf2_low and elf2_low <= elf1_high or elf2_low <= elf1_low and elf1_low <= elf2_high:
                counter += 1
    print(counter)
    
count_overlaps()