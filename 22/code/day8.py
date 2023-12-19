import numpy as np

def part1(forest, rows, cols):
    trees = 0
    for row in range(rows):
        for col in range(cols):
            h = forest[row, col]
            
            if col == 0 or np.amax(forest[row, :col]) < h:
                trees += 1
            elif col == cols - 1 or np.amax(forest[row, (col + 1):]) < h:
                trees += 1
            elif row == 0 or np.amax(forest[:row, col]) < h:
                trees += 1
            elif row == rows - 1 or np.amax(forest[(row + 1):, col]) < h:
                trees += 1
    print(trees)

def part2(forest, rows, cols):
    max_trees = 0
    # for every tree, check how many trees can be seen from it
    for row in range(rows):
        for col in range(cols):
            height = forest[row, col]
            left, right, up, down = 0, 0, 0, 0
            for i in range(1, rows):
                if row - i < 0:
                    break
                if forest[row - i, col] < height:
                    left += 1
                elif forest[row - i, col] >= height:
                    left += 1
                    break
            for i in range(1, rows):
                if row + i >= rows:
                    break
                if forest[row + i, col] < height:
                    right += 1
                elif forest[row + i, col] >= height:
                    right += 1
                    break
            for i in range(1, cols):
                if col - i < 0:
                    break
                if forest[row, col - i] < height:
                    up += 1
                elif forest[row, col - i] >= height:
                    up += 1
                    break
            for i in range(1, cols):
                if col + i >= cols:
                    break
                if forest[row, col + i] < height:
                    down += 1
                elif forest[row, col + i] >= height:
                    down += 1
                    break
                
            current = left * right * up * down
            if current > max_trees:
                max_trees = current

    print(max_trees)

if __name__ == "__main__":
    with open("input/day8.txt", "r") as f:
        lines = f.read().strip().split()
        
    forest = [list(map(int, list(line))) for line in lines]
    rows = len(forest)
    cols = len(forest[0])
    forest = np.array(forest)

    part1(forest, rows, cols)
    part2(forest, rows, cols)