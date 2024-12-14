from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr
from itertools import combinations

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 5 * 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for _ in range(t):
        N = int(input())
        points = []
        for _ in range(N):
            x = int(input())
            y = int(input())
            points.append((x, y))
        min_area = INF
        for k in range(0, 3):
            for subset in combinations(points, N - k):
                min_x = min(p[0] for p in subset)
                max_x = max(p[0] for p in subset)
                min_y = min(p[1] for p in subset)
                max_y = max(p[1] for p in subset)
                side = max(max_x - min_x + 2, max_y - min_y + 2)
                area = side * side
                if area < min_area:
                    min_area = area
        answer = min_area
        answers.append(f"{answer}")
    print(*answers, sep="\n")