from base64 import b64decode, b64encode
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

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep="\n", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        x = input().decode()
        cards = [f"{i}{j}{k}" for i, j, k in zip(x[::3], x[1::3], x[2::3])]
        shape_count = [13, 13, 13, 13]
        card_count = [[0] + [1 for _ in range(13)] for _ in range(4)]
        for card in cards:
            shape, number = card[0], int(card[1:])
            shape_count["PKHT".index(shape)] -= 1
            card_count["PKHT".index(shape)][number] -= 1
        if any(any(i < 0 for i in v) for v in card_count):
            answer = "GRESKA"
        else:
            answer = " ".join(map(str, shape_count))
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")