from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import cmp_to_key
from itertools import combinations, permutations, product
from math import sqrt
from sys import stdout, stderr

getcontext().prec = 30


def is_jolly(n, sequence):
    if n == 1:
        return True
    differences = sorted(set(abs(i - j) for i, j in zip(sequence, sequence[1:])))
    expected_differences = sorted(range(1, n))
    return differences == expected_differences


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
    t = INF
    answers = []
    for hh in range(1, t + 1):
        s = input()
        if s is None:
            break
        n = int(s)
        numbers = [int(input()) for _ in range(n)]
        answer = "Jolly" if is_jolly(n, numbers) else "Not jolly"
        answers.append(f"{answer}")
    print(*answers, sep="\n")