from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        variables = {'B': [], 'E': [], 'S': [], 'I': [], 'G': [], 'O': [], 'M': []}
        for _ in range(N):
            var, val = input(), int(input())
            variables[var].append(val)
        counts = {}
        for var in variables:
            evens = sum(1 for x in variables[var] if x % 2 == 0)
            odds = len(variables[var]) - evens
            counts[var] = (evens, odds)
        total = 1
        for var in variables:
            total *= len(variables[var])
        B_even, B_odd = counts['B']
        I_even, I_odd = counts['I']
        bi_odd = B_even * I_odd + B_odd * I_even
        G_even, G_odd = counts['G']
        O_even, O_odd = counts['O']
        E_even, E_odd = counts['E']
        S_even, S_odd = counts['S']
        C1 = G_odd * O_even * E_even * S_even + G_even * O_odd * E_even * S_even + G_even * O_even * E_odd * S_even + G_even * O_even * E_even * S_odd
        C3 = G_odd * O_odd * E_odd * S_even + G_odd * O_odd * E_even * S_odd + G_odd * O_even * E_odd * S_odd + G_even * O_odd * E_odd * S_odd
        goe_s_odd = C1 + C3
        M_even, M_odd = counts['M']
        assignments_odd = bi_odd * goe_s_odd * M_odd
        answer = total - assignments_odd
        answers.append(f"{answer}")
    print(*answers)
