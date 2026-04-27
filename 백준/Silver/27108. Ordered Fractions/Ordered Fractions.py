from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import cmp_to_key
from itertools import combinations, permutations, product
from math import sqrt
from sys import stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        answer_list = sorted(set([Fraction(i, j) for i, j in product(range(N + 1), repeat=2) if not (i == j == 0) and i <= j]))
        answer = f"{len(answer_list)}\n" + "\n".join([f"{i.numerator}/{i.denominator}" for i in answer_list])
        answers.append(f"{answer}")
    print(*answers, sep="\n")