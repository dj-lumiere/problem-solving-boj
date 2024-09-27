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
        N = int(input())
        commands = [int(input()) for _ in range(N)]
        stop_key = int(input())
        positions = list(range(8))
        for cmd in commands:
            for i in range(7):
                for j in range(i + 1, 8):
                    if cmd == (2 ** i + 2 ** j):
                        i_index = positions.index(i)
                        j_index = positions.index(j)
                        positions[i_index], positions[j_index] = positions[j_index], positions[i_index]
        answer = positions.index(stop_key)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
