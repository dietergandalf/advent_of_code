
def solve(part, file):
    with open(file) as f:
        data = f.readlines()
    for i, line in enumerate(data):
        data[i] = list(map(int, line.split()))

    next_numbers = []
    for line in data:
        row = line
        all_rows = []
        all_rows.append(row)
        while True:
            differences = []
            for i in range(len(row) - 1):
                diff = row[i + 1] - row[i]
                differences.append(diff)
            all_rows.append(differences)

            all_zeros = True
            for num in differences:
                if num != 0:
                    all_zeros = False
                    row = differences
                    break
            if all_zeros:
                break

        if part == 1:
            for i, row in enumerate(all_rows[::-1]):
                if i == 0:
                    row.append(0)
                    continue
                row.append(all_rows[::-1][i - 1][-1] + row[-1])
            next_numbers.append(all_rows[0][-1])
        else: # part 2
            for i, row in enumerate(all_rows[::-1]):
                print(row)
                if i == 0:
                    row.append(0)
                    continue
                row.insert(0, row[0] - all_rows[::-1][i - 1][0])
            next_numbers.append(all_rows[0][0])
        print(all_rows)
    print(sum(next_numbers))


solve(2, '23/input/day9_test.txt')
solve(2, '23/input/day9.txt')