import os

PATH = os.getcwd()

def createFiles(year, day=None):
    #folders per year
    
    if not os.path.exists(f"{PATH}/{year}"):
        os.mkdir(f"{PATH}/{year}")
    if not os.path.exists(f"{PATH}/{year}/code"):
        os.mkdir(f"{PATH}/{year}/code")
    if not os.path.exists(f"{PATH}/{year}/input"):
        os.mkdir(f"{PATH}/{year}/input")

    #files per day
    if day is None:
        for day in range(1, 26):
            createFiles(year, day)
        return
    path_py = f"{PATH}/{year}/code/day{day}.py"
    path_input = f"{PATH}/{year}/input/day{day}.txt"
    path_test = path_input.replace(".txt", "_test.txt")

    #files
    if not os.path.exists(path_py):
        with open(path_py, "w") as f:
            f.write(f"# Day {day} Advent of Code {year}\n\ndef solve(file, part=0):\n   pass\n\nif __name__ == '__main__':\n   solve('{path_test}', 0)\n   #solve('{path_input}', 0)\n")
    if not os.path.exists(path_input):
        with open(path_input, "w") as f:
            f.write(f"")
        with open(path_test, "w") as f:
            f.write(f"")



if __name__ == "__main__":
    usage = "Usage: python aoc.py [year] [day(optional)]"
    import sys
    if len(sys.argv) == 1:
        print(usage)
        exit()
    year = sys.argv[1]
    if len(sys.argv) == 2:
        createFiles(year)
    else:
        day = sys.argv[2]
        createFiles(year, day)