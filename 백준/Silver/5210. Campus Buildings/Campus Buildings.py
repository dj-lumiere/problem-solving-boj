from bisect import bisect_left
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
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        words = []
        for _ in range(n):
            words.append(input().decode())
        target = input().decode()
        answer = [f"Data Set {hh+1}:"]
        for word in words:
            lcs = [[0 for _ in range(len(target)+1)] for _ in range(len(word)+1)]
            for j, v2 in enumerate(target.upper(), start=1):
                for i, v in enumerate(word.upper(), start=1):
                    if v == v2:
                        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1]+1)
                    else:
                        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            eprint(lcs)
            if lcs[-1][-1] == len(target):
                answer.append(word)
        answers.append("\n".join(answer))
    print(answers)