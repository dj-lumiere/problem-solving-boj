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
    t = INF
    answers = []
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        m = list(str(n))
        max_digit = max(m)
        for idx, ch in enumerate(m):
            if ch == max_digit:
                D = int(ch)
                if D % 2 == 1:
                    m[idx] = '0'
                else:
                    D += 4
                    if D > 9:
                        D = D % 10
                    m[idx] = str(D)
                break
        answer = int(''.join(m))
        answers.append(f"{answer}")
    print(*answers, sep="\n")