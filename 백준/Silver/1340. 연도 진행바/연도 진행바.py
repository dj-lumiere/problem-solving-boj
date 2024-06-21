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


def invert_case(x: str):
    result = ""
    for v in x:
        if not v.isalpha():
            result += v
        elif v.isupper():
            result += v.lower()
        elif v.islower():
            result += v.upper()
    return result


def remove_number(x: str):
    result = ""
    for v in x:
        if not v.isdigit():
            result += v
    return result


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    for hh in range(t):
        m, d, y, hm = input().decode().split()
        d = d[:-1]
        h, n = hm.split(":")
        current = datetime(int(y), [i+1 for i,v in enumerate(month) if v == m][0], int(d), int(h), int(n),0,0)
        answer = (current-datetime(int(y),1,1,0,0,0,0))/(datetime(int(y)+1,1,1,0,0,0,0)-datetime(int(y),1,1,0,0,0,0))*100
        answers.append(f"{answer}")
    print(answers)