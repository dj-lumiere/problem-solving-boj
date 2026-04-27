from time import perf_counter_ns, sleep
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, ("sep".join(map(str, args)) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    numbers = []
    for h in range(t):
        pass
    while True:
        try:
            numbers.extend(map(int, input().split()))
        except:
            answer = max(gcd(i, j) for i, j in combinations(numbers, 2))
            answers.append(f"{answer}")
            break
    print(answers)