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
        n, m = int(input()), int(input())
        A = [0] * n
        for i in range(n):
            A[i] = int(input())
        B = [0] * m
        for i in range(m):
            B[i] = int(input())
        votes = [0] * n
        for j in range(m):
            best_match = -1
            for i in range(n):
                if A[i] <= B[j]:
                    if best_match == -1 or i < best_match:
                        best_match = i
            votes[best_match] += 1
        most_voted_game = 0
        for i in range(1, n):
            if votes[i] > votes[most_voted_game]:
                most_voted_game = i
        answers.append(most_voted_game + 1)
    print(*answers, sep="\n")
