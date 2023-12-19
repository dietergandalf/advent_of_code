class Card:
    def __init__(self, input: str):
        self.amount = 1
        self.points = 0
        self.matching = 0
        card, values = input.split(":")
        card = card.replace("  ", " ")
        card = card.replace("  ", " ")
        card = card.split(" ")
        self.card = int(card[1])
        winning, have = values.split("|")
        self.winning = []
        for value in winning.split(" "):
            if value != "" and value != " ":
                self.winning.append(int(value))
        self.have = []
        for value in have.split(" "):
            if value != "" and value != " ":
                self.have.append(int(value))
        self.have.sort()
        self.winning.sort()
        self.calculatePoints()

    def getMatching(self):
        self.matching = 0
        for value in self.have:
            if value in self.winning:
                self.matching += 1

    def calculatePoints(self):
        self.points = 0
        self.getMatching()
        for i in range(self.matching):
                if self.points == 0:
                    self.points = 1
                else:
                    self.points *= 2

    def useCard(self, cards):
        for i in range(self.matching):
            cards[self.card + i].amount += self.amount
                


    def __str__(self):
        return f"Card {self.card}, Matching {self.matching} Amount {self.amount}"



with open("input/day4.txt") as f:
    cards = [Card(line) for line in f.readlines()]
sum = 0
for card in cards:
    sum += card.points
print(sum)

total = 0
for card in cards:
    card.useCard(cards)
    total += card.amount
for card in cards:
    print(card)
print(total)

