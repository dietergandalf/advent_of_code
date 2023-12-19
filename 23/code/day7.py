letter_map_a = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}
letter_map_b = {'T': 'A', 'J': '1', 'Q': 'C', 'K': 'D', 'A': 'E'}

def score(hand: str) -> int:
    counts = [hand.count(c) for c in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if 2 in counts:
        if counts.count(2) == 4:
            return 2
        return 1
    return 0

def classify(task_part, hand: str) -> int:
    curr_score = score(hand)
    if task_part == 'a':
        return curr_score
    jokers = hand.count('J')
    if jokers == 0:
        return curr_score
    for card in hand:
        if card == 'J':
            continue
        tester = hand.replace('J', card)
        if score(tester) > curr_score:
            curr_score = score(tester)
    return curr_score

def strength(task_part, hand: str) -> tuple[int, list[str]]:
    if task_part == 'a':
        letter_map = letter_map_a
    else:
        letter_map = letter_map_b
    return (classify(task_part, hand), [letter_map.get(c, c) for c in hand])

def solve(task_part, file: str) -> int:
    with open(file) as f:
        lines = f.readlines()
    plays = []
    for line in lines:
        hand, bid = line.strip().split()
        plays.append((hand, int(bid)))
    plays.sort(key = lambda play: strength(task_part, play[0]))
    sum = 0
    for i, play in enumerate(plays, 1):
        sum += play[1] * i
    return sum

if __name__ == '__main__':
    print(solve('a', 'input/day7_test.txt'))
    print(solve('b', 'input/day7.txt'))
