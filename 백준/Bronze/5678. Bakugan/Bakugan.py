from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import cmp_to_key
from itertools import permutations
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
    t = INF
    answers = []
    for hh in range(1, t + 1):
        R = int(input())
        if R == 0:
            break
        mark_monsters = list(map(int, input().split()))
        leti_monsters = list(map(int, input().split()))
        mark_points = sum(mark_monsters)
        leti_points = sum(leti_monsters)
        for (i1,j1,k1), (i2,j2,k2) in zip(zip(mark_monsters, mark_monsters[1:], mark_monsters[2:]), zip(leti_monsters, leti_monsters[1:], leti_monsters[2:])):
            mark_consecutive = (i1 == j1 == k1)
            leti_consecutive = (i2 == j2 == k2)
            if mark_consecutive and leti_consecutive:
                break
            if mark_consecutive and not leti_consecutive:
                mark_points += 30
                break
            if leti_consecutive and not mark_consecutive:
                leti_points += 30
                break
        if mark_points > leti_points:
            answer = "M"
        elif leti_points > mark_points:
            answer = "L"
        else:
            answer = "T"
        answers.append(f"{answer}")
    print(*answers, sep="\n")