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
    t = INF
    answers = []
    for hh in range(t):
        n = input()
        b = input()
        m = input()
        if n is None or b is None or m is None:
            break
        n = Decimal(n)
        b = Decimal(b)
        m = Decimal(m)
        y = 0
        while n <= m:
            n += n * b / 100
            y += 1
        answer = y
        answers.append(f"{answer}")
    print(*answers, sep="\n")