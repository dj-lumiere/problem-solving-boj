from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    for hh in range(t):
        n = input().decode().split()
        if n == ["#"]:
            break
        start, *progress = n
        answer = "Draw"
        grid = ["" for _ in range(10)]
        for i, v in enumerate(map(int, progress)):
            current_turn = ""
            if (start == "X" and i % 2 == 1) or (start == "O" and i % 2 == 0):
                current_turn = "O"
            else:
                current_turn = "X"
            grid[v] = current_turn
            if any(all(grid[j] == grid[i[0]] != "" for j in i) for i in
                   [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]):
                answer = current_turn
                break
        answers.append(f"{answer}")
    print(answers)