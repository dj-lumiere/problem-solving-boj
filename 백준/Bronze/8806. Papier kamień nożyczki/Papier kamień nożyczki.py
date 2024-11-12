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
    t = int(input())
    answers = []
    for hh in range(t):
        X1, Y1, Z1 = map(Decimal, [input(), input(), input()])
        X2, Y2, Z2 = map(Decimal, [input(), input(), input()])
        p_tie = X1 * X2 + Y1 * Y2 + Z1 * Z2
        p_adam = X1 * Y2 + Y1 * Z2 + Z1 * X2
        p_gosia = X2 * Y1 + Y2 * Z1 + Z2 * X1
        if p_adam > p_gosia:
            answer = "ADAM"
        elif p_gosia > p_adam:
            answer = "GOSIA"
        else:
            answer = "="
        answers.append(f"{answer}")
    print(*answers, sep="\n")