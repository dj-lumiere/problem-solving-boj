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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        def sum_of_squares(n):
            return sum(int(digit) ** 2 for digit in str(n))
        def is_happy(n):
            visited = set()
            while n != 1 and n not in visited:
                visited.add(n)
                n = sum_of_squares(n)
            return n == 1
        n = int(input())
        if is_happy(n):
            answers.append("HAPPY")
        else:
            answers.append("UNHAPPY")
    print(*answers, sep="\n")
