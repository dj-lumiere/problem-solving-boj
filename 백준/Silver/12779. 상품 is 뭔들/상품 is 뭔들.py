from fractions import Fraction
from math import isqrt
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        a = int(input())
        b = int(input())
        sqrt_b = isqrt(b)
        sqrt_a = isqrt(a)
        if sqrt_a ** 2 == a:
            count = sqrt_b - sqrt_a
        else:
            count = sqrt_b - sqrt_a
        total = b - a
        if count == 0:
            answer = "0"
        else:
            frac = Fraction(count, total)
            answer = f"{frac.numerator}/{frac.denominator}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")