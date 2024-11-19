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
        max_volume = Decimal(0)
        for _ in range(n):
            type_fig = input()
            if type_fig == 'C':
                r = Decimal(input())
                h = Decimal(input())
                volume = (Decimal(1) / Decimal(3)) * Decimal('3.14159') * r * r * h
            elif type_fig == 'L':
                r = Decimal(input())
                h = Decimal(input())
                volume = Decimal('3.14159') * r * r * h
            elif type_fig == 'S':
                r = Decimal(input())
                volume = (Decimal(4) / Decimal(3)) * Decimal('3.14159') * r * r * r
            if volume > max_volume:
                max_volume = volume
        answer = "{0:.3f}".format(max_volume)
        answers.append(f"{answer}")
    print(*answers, sep="\n")