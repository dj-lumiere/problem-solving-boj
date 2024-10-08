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
        n = int(input())
        result_set = set()
        s = input()
        for j in range(len(s)):
            result_set.add(s[j:])
        for i in range(1, n):
            s = input()
            for j in range(len(s)):
                suffix = s[j:]
                if suffix in result_set:
                    result_set.remove(suffix)
                else:
                    result_set.add(suffix)
        answers.append(len(result_set))
    print(*answers, sep="\n")
