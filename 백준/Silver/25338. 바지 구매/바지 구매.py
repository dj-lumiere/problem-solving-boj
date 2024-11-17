from math import sqrt
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
        a, b, c, d = int(input()), int(input()), int(input()), int(input())
        N = int(input())
        t_val = sqrt((c - d) / (-a))
        count = 0
        for _ in range(N):
            u, v = int(input()), int(input())
            if v >= b:
                if v <= b + t_val:
                    if u == a * (v - b) ** 2 + c:
                        count += 1
                else:
                    if u == d:
                        count += 1
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")