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
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n, m = int(input()), int(input())
        category = ['kor', 'eng', 'math','apple', 'pear', 'orange','red', 'blue', 'green']
        query = {i:set() for i in category}
        for i in range(n):
            a, b, c = [input().decode() for _ in range(3)]
            query[a].add(i)
            query[b].add(i)
            query[c].add(i)
        answersub = []
        for _ in range(m):
            a,b,c = [input().decode() for _ in range(3)]
            result = set(range(n))
            if a != "-":
                result = result.intersection(query[a])
            if b != "-":
                result = result.intersection(query[b])
            if c != "-":
                result = result.intersection(query[c])
            answersub.append(len(result))
        answer = "\n".join(map(str,answersub))
        answers.append(f"{answer}")
    print(answers)