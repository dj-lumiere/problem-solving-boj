from decimal import Decimal
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
        n = int(input())
        o = int(input())
        possible = []
        for r in range(n):
            if (o - r) >= 0 and (o - r) % (n - 1) == 0:
                q = (o - r) // (n - 1)
                t_val = n * q + r
                possible.append(t_val)
        if possible:
            min_t = min(possible)
            max_t = max(possible)
            answer = f"{min_t} {max_t}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")