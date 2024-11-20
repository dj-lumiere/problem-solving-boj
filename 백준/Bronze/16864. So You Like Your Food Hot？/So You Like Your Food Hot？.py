from bisect import bisect_right
from decimal import Decimal
from itertools import product
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        pt, p1, p2 = (Decimal(input()) for _ in range(3))
        pt_cents, p1_cents, p2_cents = int(pt * 100), int(p1 * 100), int(p2 * 100)
        combinations = []
        for pitas in range(pt_cents // p1_cents + 1):
            rem = pt_cents - pitas * p1_cents
            if rem % p2_cents == 0:
                pizzas = rem // p2_cents
                combinations.append(f"{pitas} {pizzas}")
        if combinations:
            answer = '\n'.join(combinations)
        else:
            answer = "none"
        answers.append(f"{answer}")
    print(*answers, sep="\n")