from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import product, chain, permutations, combinations, repeat
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt
from heapq import heappush, heappop


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
    T = 1
    answers = []
    for hh in range(1, T + 1):
        board = [input() for _ in range(8)]
        queens = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == '*':
                    queens.append((i, j))
        if len(queens) != 8:
            answers.append("invalid")
        else:
            valid = True
            for i in range(8):
                x1, y1 = queens[i]
                for j in range(i + 1, 8):
                    x2, y2 = queens[j]
                    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                answers.append("valid")
            else:
                answers.append("invalid")
    print(*answers, sep="\n")
