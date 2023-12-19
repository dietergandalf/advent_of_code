translatea = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
translateb = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "lose", "Y": "draw", "Z": "win"}
value = {"Rock": 1, "Paper": 2, "Scissors": 3}

lose = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
win = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}

def return_corresponding_value(player1, result) -> str:
    if result == "win":
        return win[player1]
    elif result == "lose":
        return lose[player1]
    return player1

def logic(player1, player2) -> int:
    if player1 == player2:
        return 3 + value[player1]
    elif player1 == "Rock" and player2 == "Scissors":
        return value[player2]
    elif player1 == "Paper" and player2 == "Rock":
        return value[player2]
    elif player1 == "Scissors" and player2 == "Paper":
        return value[player2]
    elif player2 == "Rock" and player1 == "Scissors":
        return 6 + value[player2]
    elif player2 == "Paper" and player1 == "Rock":
        return 6 + value[player2]
    elif player2 == "Scissors" and player1 == "Paper":
        return 6 + value[player2]



points1 = 0
points2 = 0
with open("input/day2.txt", "r") as f:
    data = f.read()
    data_per_round = data.split("\n")
    # Part 1
    for data in data_per_round:
        player1, player2 = data.split(" ")
        points1 += logic(translatea[player1], translatea[player2])
    print(points1)
    
    # Part 2
    for data in data_per_round:
        player1, result = data.split(" ")
        player1 = translateb[player1]
        result = translateb[result]
        player2 = return_corresponding_value(player1, result)
        points2 += logic(player1, player2)
print(points2)