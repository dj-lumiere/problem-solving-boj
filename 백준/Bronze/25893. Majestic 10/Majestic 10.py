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
        for _ in range(n):
            a, b, c = input(), input(), input()
            stats = [int(a), int(b), int(c)]
            count = sum(stat >= 10 for stat in stats)
            if count == 0:
                msg = "zilch"
            elif count == 1:
                msg = "double"
            elif count == 2:
                msg = "double-double"
            else:
                msg = "triple-double"
            answer = f"{a} {b} {c}\n{msg}\n"
            answers.append(f"{answer}")
    print(*answers, sep="\n")