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
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        gold_medals = [0 for _ in range(2022)]
        all_medals = [0 for _ in range(2022)]
        for _ in range(n):
            year, _, medal = int(input()), input(), input().decode()
            if medal == "Gold":
                gold_medals[year] += 1
            all_medals[year] += 1
        answer = f"{gold_medals.index(max(gold_medals))} {all_medals.index(max(all_medals))}"
        answers.append(f"{answer}")
    print(answers)