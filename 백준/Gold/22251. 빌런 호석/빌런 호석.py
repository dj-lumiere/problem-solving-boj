from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt

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
    led_segment = [
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1],
    ]
    for hh in range(1, t + 1):
        n, k, p, x = (int(input()) for _ in range(4))
        current_config = [led_segment[y] for y in map(int, str(x).rjust(k, "0"))]
        answer = 0
        for i in range(1, n + 1):
            if i == x:
                continue
            target_config = [led_segment[y] for y in map(int, str(i).rjust(k, "0"))]
            toggle_led_count = sum([sum(v3 != v4 for v3, v4 in zip(v1, v2)) for v1, v2 in
                                    zip(current_config, target_config)])
            if toggle_led_count <= p:
                answer += 1
        answers.append(answer)
    print(*answers, sep="\n")
