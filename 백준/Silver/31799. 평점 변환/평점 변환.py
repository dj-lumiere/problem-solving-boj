from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        x = re.split("(A\+|A\-|A0|B\+|B\-|B0|C\+|C\-|C0|A|B|C)", input().decode())
        x = [i for i in x if i]
        for i, v in enumerate(x):
            if v in ["A", "B", "C"]:
                x[i] = v + "0"
        answer = ""
        for i, v in enumerate(x):
            if v in ["C+", "C0", "C-"]:
                answer += "B"
            elif v in ["B0", "B-"]:
                if i == 0 or x[i - 1] in ["C+", "C0", "C-"]:
                    answer += "D"
                else:
                    answer += "B"
            elif v in ["A-", "B+"]:
                if i == 0 or x[i - 1] in ["B0", "B-", "C+", "C0", "C-"]:
                    answer += "P"
                else:
                    answer += "D"
            elif v == "A0":
                if i == 0 or x[i - 1] in ["A-", 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']:
                    answer += "E"
                else:
                    answer += "P"
            elif v == "A+":
                answer += "E"
        answers[h] = f"{answer}"
    print(answers)