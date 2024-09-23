from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from math import sqrt
from sys import stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
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
    for hh in range(t):
        first_rate = int(input())
        additional_rate = int(input())
        n = int(input())
        for _ in range(n):
            consumption = int(input())
            if consumption <= 1000:
                charges = consumption * first_rate
            else:
                charges = (1000 * first_rate) + ((consumption - 1000) * additional_rate)
            answers.append(f"{consumption} {charges}")
    print(*answers, sep="\n")