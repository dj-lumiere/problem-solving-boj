from decimal import Decimal, getcontext
from fractions import Fraction
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
        n, p, q, r, s, a1 = (int(input()) for _ in range(6))
        table = [0, a1] + [0] * 19
        for i, v in enumerate(table):
            if i < 2:
                continue
            if i % 2 == 1:
                table[i] = table[i // 2] * r + s
            else:
                table[i] = table[i // 2] * p + q
        eprint(table)
        answer = sum(table[:n + 1])
        answers.append(f"{answer}")
    print(*answers, sep="\n")