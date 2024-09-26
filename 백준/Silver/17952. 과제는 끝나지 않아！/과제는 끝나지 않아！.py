from collections import deque
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
from sys import stdout, stderr

getcontext().prec = 30


def factors(n):
    factors = {1, n}
    for i in range(2, isqrt(n) + 1):
        if n % i != 0:
            continue
        factors.add(i)
        factors.add((n // i))
    return factors


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
    for hh in range(1, t + 1):
        N = int(input())
        stack = []
        total_score = 0
        for _ in range(N):
            q = int(input())
            if q == 0:
                if stack:
                    score, remaining_time = stack.pop()
                    remaining_time -= 1
                    if remaining_time > 0:
                        stack.append((score, remaining_time))
                    else:
                        total_score += score
            else:
                A, T = int(input()), int(input())
                if T > 1:
                    stack.append((A, T - 1))
                else:
                    total_score += A
        answer = total_score
        answers.append(f"{answer}")
    print(*answers, sep="\n")