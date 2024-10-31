from fractions import Fraction
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        deck = {2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16, 11: 4}
        sum_cards = 0
        for _ in range(n):
            card = int(input())
            sum_cards += card
            deck[card] -= 1
        x = 21 - sum_cards
        if x < 0:
            answer = "DOSTA"
        else:
            greater = sum(count for val, count in deck.items() if val > x)
            lesser = sum(count for val, count in deck.items() if val <= x)
            answer = "DOSTA" if greater >= lesser else "VUCI"
        answers.append(f"{answer}")
    print(*answers, sep="\n")