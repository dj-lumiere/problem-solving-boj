from sys import stdin
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    word = """@@@ @
@ @ @
@ @ @
@ @ @
@ @@@""".split("\n")
    for hh in range(t):
        n = int(input())
        grid = [["" for _ in range(5 * n)] for _ in range(5 * n)]
        for x, y in product(range(5), repeat=2):
            for x2, y2 in product(range(n), repeat=2):
                grid[y * n + y2][x * n + x2] = word[y][x]
        answer = "\n".join("".join(x) for x in grid)
        answers.append(f"{answer}")
    print(*answers)
