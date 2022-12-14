
def get_priority(c: str) -> int:
    if c.islower():
        return 1 + (ord(c) - ord('a'))
    else:
        return 27 + (ord(c) - ord("A"))

def get_badge_priorities(lines: list[str]) -> list[int]:
    # for every 3 lines in the input, we need to find the one character present in all 3 lines
    priorities = []
    # split lines into lists of 3 lines
    list_of_3_lines = [lines[i:i+3] for i in range(0, len(lines), 3)]
    # for each list of 3 lines, find the character that is present in all 3 lines
    for list in list_of_3_lines:
        print(list)
        # for each character in the first line, check if it is present in the other 2 lines
        for c in list[0]:
            if c in list[1] and c in list[2]:
                priorities.append(get_priority(c))
                break   # we only want to add it once
    return priorities


# Part 1
def get_doubled_item_priority(s: str) -> int:
    # s0 = first half of s
    s0 = s[:len(s)//2]
    s1 = s[len(s)//2:]
    for c in s0:
        if c in s1:
            return get_priority(c)

# Part 1
with open("input/day3.txt", "r") as f:
    s = f.read()
    lines = s.splitlines()
    sums = [get_doubled_item_priority(line) for line in lines]
    print(sum(sums))
    
#Part 2
with open("input/day3.txt", "r") as f:
    s = f.read()
    lines = s.splitlines()
    sums2 = get_badge_priorities(lines)
    print(sums2)
    print(sum(sums2))