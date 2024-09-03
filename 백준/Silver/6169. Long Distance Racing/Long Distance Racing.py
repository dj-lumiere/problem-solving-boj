from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        m, t, u, f, d = (int(input()) for _ in range(5))
        path_time = {"u": u, "f": f, "d": d}
        path = [input() for _ in range(t)]
        path_reverse = ["d" if s == "u" else ("u" if s == "d" else s) for s in path]
        race_time = [path_time[x] + path_time[y] for x, y in zip(path, path_reverse)]
        race_time_accumulate = [0 for _ in range(t)]
        for i, v in enumerate(race_time):
            race_time_accumulate[i] = race_time_accumulate[i - 1] + v
        eprint(race_time_accumulate)
        answer = bisect_right(race_time_accumulate, m)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
