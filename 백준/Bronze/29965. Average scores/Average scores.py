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
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        mari_score = 0
        mari_playcount = 0
        juri_score = 0
        juri_playcount = 0
        for _ in range(n):
            player, score = input().decode(), int(input())
            if player == "M":
                mari_score += score
                mari_playcount += 1
            elif player == "J":
                juri_score += score
                juri_playcount += 1
        mari_average = mari_score / mari_playcount if mari_playcount else 0
        juri_average = juri_score / juri_playcount if juri_playcount else 0
        answer = "V"
        if mari_average > juri_average:
            answer = "M"
        elif mari_average < juri_average:
            answer = "J"
        answers[h] = f"{answer}"
    print(answers)