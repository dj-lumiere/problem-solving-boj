from decimal import Decimal
from math import isqrt
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        b, w = int(input()), int(input())
        max_s = 0
        total = b + w
        max_possible = int(isqrt(total))
        for s in range(1, max_possible + 1):
            half = s * s // 2
            other = s * s - half
            if (b >= half and w >= other) or (w >= half and b >= other):
                max_s = s
        if max_s == 0:
            answer = "Impossible"
        else:
            answer = f"{max_s}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")