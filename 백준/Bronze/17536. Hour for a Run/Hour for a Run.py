from bisect import bisect_right
from math import ceil
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        m = int(input())
        result = " ".join(map(str, [ceil(n * m / 10 * i) for i in range(1, 10)]))
        answer = f"{result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")