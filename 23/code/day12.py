cache = {}

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in cfg else 1
    
    key = (cfg, nums)
    if key in cache:
        return cache[key]

    result = 0
    if cfg[0] in ".?":
        result += count(cfg[1:], nums)
    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0]+1:], nums[1:])
    
    cache[key] = result
    return result

def solve(file, part=1):
    with open(file) as f:
        data = f.read().splitlines()
    total = 0
    for line in data:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        if part == 2:
            cfg = "?".join([cfg]*5)
            nums = nums * 5
        total += count(cfg, nums)
    print(total)
    

solve("23/input/day12_test.txt", 2)
solve("23/input/day12.txt", 2)