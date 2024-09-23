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
        n = int(input())
        a = int(input())
        b = int(input())
        log_entries = [int(input()) for _ in range(n - 1)]
        if a > min(log_entries) or max(log_entries) > b:
            answer = -1
            answers.append(f"{answer}")
            break
        has_min = a in log_entries
        has_max = b in log_entries
        possible_values = []
        if not has_min and not has_max:
            answer = -1
            answers.append(f"{answer}")
            break
        if not has_min:
            possible_values.append(a)
        if not has_max:
            possible_values.append(b)
        if has_min and has_max:
            possible_values.extend(range(a, b + 1))
        possible_values = sorted(set(possible_values))
        if possible_values:
            answer = "\n".join(map(str, possible_values))
        else:
            answer = -1
        answers.append(f"{answer}")
    print(*answers, sep="\n")