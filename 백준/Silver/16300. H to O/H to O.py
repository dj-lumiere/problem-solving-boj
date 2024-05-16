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
        elements = re.split("([A-Z])", input().decode())
        element_count = {}
        current_atom = ""
        for i, v in enumerate(elements):
            if v.isalpha():
                current_atom = v
                continue
            if v == '':
                element_count[current_atom] = element_count.get(current_atom, 0) + 1
            if v.isdigit():
                element_count[current_atom] = element_count.get(current_atom, 0) + int(v)
        element_count.pop('')
        n = int(input())
        for k, v in element_count.items():
            element_count[k] = v * n
        target = re.split("([A-Z])", input().decode())
        target_count = {}
        current_atom = ""
        for i, v in enumerate(target):
            if v.isalpha():
                current_atom = v
                continue
            if v == '':
                target_count[current_atom] = target_count.get(current_atom, 0) + 1
            if v.isdigit():
                target_count[current_atom] = target_count.get(current_atom, 0) + int(v)
        target_count.pop('')
        answer = 1231231231234
        for k, v in target_count.items():
            answer = min(answer, element_count.get(k, 0) // v)
        answers.append(f"{answer}")
    print(answers)