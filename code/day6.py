
def find_first_x_nonduplicate_characters(string: str, x: int):
    """Find the first x non-duplicate characters in a string."""
    for i in range(len(string)-(x+1)):
        s = string[i:i+x]
        count = 0
        for c in s:
            if s.count(c) == 1:
                count += 1
            if count == x:
                print(i+x)
                return string[i:i+x]
    return None
    

with open("input/day6.txt") as f:
    data = f.read()
    print(find_first_x_nonduplicate_characters(data, 14))