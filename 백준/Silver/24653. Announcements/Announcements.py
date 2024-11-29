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
        N = int(input())
        S = [int(input()) for _ in range(N)]
        T = int(input())
        intervals = sorted([(s, (s // T + 1) * T) for s in S], key=lambda x: x[1])
        count = 0
        last_visit = -1
        for interval in intervals:
            if last_visit < interval[0]:
                last_visit = interval[1] - 1
                count += 1
        answer = f"{count}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")