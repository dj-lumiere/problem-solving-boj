from collections import Counter
from decimal import Decimal, getcontext
from math import gcd
from random import randint
from sys import setrecursionlimit, stdout, stderr

getcontext().prec = 90

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
    t = INF
    cost_map = {"Paper": 57.99, "Printer": 120.50, "Planners": 31.25, "Binders": 22.50, "Calendar": 10.95, "Notebooks": 11.20, "Ink": 66.95}
    total_cost = 0
    answers = []
    for hh in range(t):
        item = input()
        if item == "EOI":
            break
        if item in cost_map:
            total_cost += cost_map[item]
    answer = f"${total_cost:.2f}"
    answers.append(f"{answer}")
    print(*answers, sep="\n")
