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
        x = int(input())
        l = int(input())
        r = int(input())
        prime_factors_x = factors(x)
        unlike_numbers = []
        for y in range(l, r + 1):
            if x == y:
                continue
            prime_factors_y = factors(y)
            common_factors = prime_factors_x.intersection(prime_factors_y)
            if len(common_factors) <= 2:
                unlike_numbers.append(y)
        answer = f"{len(unlike_numbers)}\n" + " ".join(map(str, unlike_numbers))
        answers.append(f"{answer}")
    print(*answers, sep="\n")