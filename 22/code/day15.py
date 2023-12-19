def a(file: str, line: int):
    with open(file) as f:
        data = f.read().splitlines()

    coords = []
    for row in data:
        row = row.split(":")
        sensor = list(map(int, row[0].replace("Sensor at x=", "").replace(" y=", "").split(",")))
        beacon = list(map(int, row[1].replace(" closest beacon is at x=", "").replace(" y=", "").split(",")))
        x_distance = sensor[0] - beacon[0]
        y_distance = sensor[1] - beacon[1]
        if x_distance < 0:
            x_distance = x_distance * -1
        if y_distance < 0:
            y_distance = y_distance * -1
        distance = x_distance + y_distance
        if distance < 0:
            distance = distance * -1
        coords.append([sensor, beacon, distance])

    count = 0
    coord_ranges = []
    for coord in coords:
        # find possible coords on the line which are still in range
        # if coords are in range, find min and max values
        # count = max - min
        if coord[0][1] > line:
            distance = coord[0][1] - line
            if distance > coord[2]:
                continue
            distance = coord[2] - distance
            coord_ranges.append((coord[0][0] - distance, coord[0][0] + distance))
        elif coord[0][1] < line:
            distance = line - coord[0][1]
            if distance > coord[2]:
                continue
            distance = coord[2] - distance
            coord_ranges.append((coord[0][0] - distance, coord[0][0] + distance))
        else:
            coord_ranges.append((coord[0][0] - coord[2], coord[0][0] + coord[2]))
    coord_ranges.sort()
    for i in range(len(coord_ranges) - 1):
        if coord_ranges[i][1] + 1 >= coord_ranges[i + 1][0] or coord_ranges[i][1] >= coord_ranges[i + 1][1]:
            coord_ranges[i + 1] = (coord_ranges[i][0], coord_ranges[i + 1][1] if coord_ranges[i + 1][1] > coord_ranges[i][1] else coord_ranges[i][1])
            coord_ranges[i] = None
    coord_ranges = list(filter(None, coord_ranges))
    for coords in coord_ranges:
        count += coords[1] - coords[0]
    #print(count)
    return coord_ranges

def b(file, maximum):
    for i in range(maximum, 0, -1):
        if len(a(file, i)) == 2:
            point = (a(file, i)[0][1]+1,i)
            print(point)
            print(point[0]*4000000+point[1])
            break

if __name__ == "__main__":
    a("22/input/day15_test.txt", 11)
    a("22/input/day15.txt", 2000000)
    b("22/input/day15_test.txt", 20)
    b("22/input/day15.txt", 4000000)