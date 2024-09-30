from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(1, t + 1):
        n, d = int(input()), int(input())
        if n == 0 and d == 0:
            break
        becs_removed = int(input())
        cas_removed = int(input())
        days_choices = [(int(input()), int(input())) for _ in range(d)]
        result = []
        becs_wardrobe = list(range(1, n + 1))
        cas_wardrobe = list(range(1, n + 1))
        if becs_removed != 0:
            del becs_wardrobe[becs_removed - 1]
        if cas_removed != 0:
            del cas_wardrobe[-cas_removed]
        result = []
        for day_num, (becs_choice, cas_choice) in enumerate(days_choices, start=1):
            becs_outfit = becs_wardrobe[becs_choice - 1]
            cas_outfit = cas_wardrobe[-cas_choice]
            if becs_outfit == cas_outfit:
                result.append(f"Day {day_num} ALERT")
            else:
                result.append(f"Day {day_num} OK")
        answers.extend([f"Scenario {hh}"]+result)
    print(*answers, sep="\n")
