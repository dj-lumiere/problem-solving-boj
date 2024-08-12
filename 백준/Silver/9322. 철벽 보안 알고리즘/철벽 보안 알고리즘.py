from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from sys import stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, pairwise, groupby, islice, starmap
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000


class MapIndex:
    def __init__(self, function, iterable):
        self.function = function
        self.iterable = iterable

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, key):
        return self.function(self.iterable[key])


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
    t = int(input())
    answers = []
    for hh in range(t):
        n = int(input())
        public1 = [input() for _ in range(n)]
        public1_order = {v: i for i, v in enumerate(public1)}
        public2 = [input() for _ in range(n)]
        public2_order = {v: i for i, v in enumerate(public2)}
        mapping_rule = {v: public2_order[i] for i, v in public1_order.items()}
        cypher_text = [input() for _ in range(n)]
        normal_text = ["" for _ in range(n)]
        for k, v in mapping_rule.items():
            normal_text[k] = cypher_text[v]
        answer = " ".join(normal_text)
        answers.append(f"{answer}")
    print(*answers, sep="\n")