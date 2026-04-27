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
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, ("sep".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        answer = n*n
        answer2 = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    answer2[i][j] = 1
                else:
                    answer2[i][j] += answer2[i-1][j]
                    answer2[i][j] += answer2[i][j-1]
        answers[h] = f"{answer2[-1][-1]} {answer}"
    print(answers)