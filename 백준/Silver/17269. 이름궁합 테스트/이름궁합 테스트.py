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
    answers = ["" for _ in range(t)]
    MOD = 998244353
    for hh in range(t):
        n, m = int(input()), int(input())
        a, b = list(input().decode()), list(input().decode())
        code = list(map(int, "32124313113132122212111221"))
        name_sync_test = ""
        for i, j in zip_longest(a, b, fillvalue=""):
            name_sync_test += i+j
        name_sync_test_list = [[code[ord(i)-ord("A")] for i in name_sync_test], []]
        for _ in range(len(name_sync_test)-2):
            for i, j in zip(name_sync_test_list[0], name_sync_test_list[0][1:]):
                name_sync_test_list[1].append((i+j)%10)
            name_sync_test_list[1], name_sync_test_list[0] = name_sync_test_list[0], name_sync_test_list[1]
            name_sync_test_list[1].clear()
        answer = name_sync_test_list[0][0]*10+name_sync_test_list[0][1]
        answers[hh] = f"{answer}%"
    print(answers)