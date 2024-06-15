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
with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    for hh in range(t):
        n = int(input())
        scores = [[int(input()) for _ in range(3)] for _ in range(n)]
        scores.sort(key=lambda x: x[2])
        gold = scores.pop()
        silver = scores.pop()
        bronze = scores.pop()
        if gold[0] == silver[0] == bronze[0]:
            while True:
                next_student = scores.pop()
                if not (gold[0] == silver[0] == next_student[0]):
                    bronze = next_student
                    break
        answer = f"{gold[0]} {gold[1]}\n{silver[0]} {silver[1]}\n{bronze[0]} {bronze[1]}"
        answers.append(f"{answer}")
    print(answers)