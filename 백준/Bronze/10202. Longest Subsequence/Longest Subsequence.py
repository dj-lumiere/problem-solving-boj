from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
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

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        a = [input().decode() for _ in range(n)]
        current_combo = [0 for _ in range(n)]
        for i, v in enumerate(a):
            if v == "X":
                current_combo[i] = current_combo[i - 1] + 1
            else:
                current_combo[i] = 0
        result = max(current_combo)
        answer = f"The longest contiguous subsequence of X's is of length {result}"
        answers.append(f"{answer}")
    print(answers)