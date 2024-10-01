from collections import deque
from sys import stdout, stderr

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
    for hh in range(1, t + 1):
        N = int(input())
        cups = []
        for _ in range(N):
            token1, token2 = input(), input()
            if token1.isdigit():
                diameter = int(token1)
                color = token2
                radius = diameter // 2
            else:
                color = token1
                radius = int(token2)
            cups.append((radius, color))
        cups.sort(key=lambda x: x[0])
        for radius, color in cups:
            answers.append(color)
    print(*answers, sep="\n")