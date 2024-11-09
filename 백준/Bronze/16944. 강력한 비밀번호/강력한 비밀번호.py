from collections import Counter
from math import gcd
from random import randint
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        s = input()
        has_digit = any(c.isdigit() for c in s)
        has_lower = any(c.islower() for c in s)
        has_upper = any(c.isupper() for c in s)
        has_special = any(c in "!@#$%^&*()-+" for c in s)
        missing_types = 0
        if not has_digit:
            missing_types += 1
        if not has_lower:
            missing_types += 1
        if not has_upper:
            missing_types += 1
        if not has_special:
            missing_types += 1
        answer = max(missing_types, 6 - len(s))
        answers.append(f"{answer}")
    print(*answers, sep="\n")