from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import cmp_to_key
from itertools import permutations
from math import sqrt
from sys import stdout, stderr

getcontext().prec = 30


def parse_fraction(s):
    if ',' in s:
        w, frac = s.split(',')
        w = int(w)
        n, d = map(int, frac.split('/'))
        numerator = w * d + n
        denominator = d
    elif '/' in s:
        n, d = map(int, s.split('/'))
        numerator = n
        denominator = d
    else:
        numerator = int(s)
        denominator = 1
    return Fraction(numerator, denominator)


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
        n = int(input())
        if n == 0:
            break
        fractions = [parse_fraction(input()) for _ in range(n)]
        fraction_sum = sum(fractions)
        if fraction_sum.denominator == 1:
            answer = f"Test {hh}: {fraction_sum.numerator}"
        elif fraction_sum < 1:
            answer = f"Test {hh}: {fraction_sum.numerator}/{fraction_sum.denominator}"
        else:
            int_part, frac_part = divmod(fraction_sum.numerator, fraction_sum.denominator)
            answer = f"Test {hh}: {int_part},{frac_part}/{fraction_sum.denominator}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")