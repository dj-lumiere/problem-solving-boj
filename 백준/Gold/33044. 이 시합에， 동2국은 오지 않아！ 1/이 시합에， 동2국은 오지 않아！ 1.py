from collections import Counter
from decimal import getcontext
from itertools import combinations, product
from math import comb
from sys import stderr, stdout

getcontext().prec = 30


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    possible_set = set()
    for i in combinations(range(1, 10), r=7):
        possible_set.add(tuple(sorted(list(i) * 2)))
    possible_body = [(i, i + 1, i + 2) for i in range(1, 8)] + [(i, i, i) for i in range(1, 10)]
    for i1, i2, i3, i4 in product(possible_body, repeat=4):
        for i5 in range(1, 10):
            deck = sorted(list(i1) + list(i2) + list(i3) + list(i4) + [i5] * 2)
            if any(deck.count(i) > 4 for i in range(1, 10)):
                continue
            possible_set.add(tuple(deck))
    possible_counter = [Counter(i) for i in possible_set]
    for hh in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        a_counter = Counter(a)
        for i in range(1, 10):
            if i not in a_counter:
                a_counter[i] = 0
        answer = 0
        for i in possible_counter:
            answer_sub = 1
            for k, v in i.items():
                answer_sub *= comb(a_counter[k], v)
            answer += answer_sub
        answers.append(f"{answer}")
    print(*answers, sep="\n")