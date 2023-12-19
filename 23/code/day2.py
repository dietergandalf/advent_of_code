class Bag:
    def __init__(self, id: int, blue: int, red: int, green:int):
        self.id = id
        self.blue = blue
        self.red = red
        self.green = green
    
MAX_RED = 12
MAX_GRREEN = 13
MAX_BLUE = 14

with open("input/day2.txt") as f:
    data = f.read().splitlines()

bags: list[Bag] = []
for line in data:
    max_red, max_blue, max_green = 0, 0, 0
    parts = line.split(":")
    parts[0] = parts[0].replace("Game ", "")
    id = int(parts[0])
    rolls = parts[1].split(";")
    for roll in rolls:
        balls = roll.split(",")
        for ball in balls:
            _, num_of_balls, color = ball.split(" ")
            num_of_balls = int(num_of_balls)
            if color == "red":
                max_red = max(max_red, num_of_balls)
            elif color == "blue":
                max_blue = max(max_blue, num_of_balls)
            elif color == "green":
                max_green = max(max_green, num_of_balls)
    bags.append(Bag(id, max_blue, max_red, max_green))

sum = 0
power, sum_of_powers = 0, 0
for bag in bags:
    if bag.blue <= MAX_BLUE and bag.red <= MAX_RED and bag.green <= MAX_GRREEN:
       sum += bag.id 

    power = bag.blue * bag.red * bag.green
    sum_of_powers += power

print(sum)
print(sum_of_powers)
