from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from inspect import stack
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        n, m = int(input()), int(input())
        candidates = []
        for _ in range(n):
            candidates.append(input())
        vote_results = {}
        for candidate in candidates:
            vote_results[candidate] = 0
        for _ in range(m):
            X = input()
            R = int(input())
            C = input()
            if X in vote_results:
                vote_results[X] += R
        max_votes = max(vote_results.values())
        winner_count = list(vote_results.values()).count(max_votes)
        if winner_count == 1:
            for candidate in vote_results:
                if vote_results[candidate] == max_votes:
                    answers.append(f"VOTE {hh}: THE WINNER IS {candidate} {vote_results[candidate]}")
                    break
        else:
            answers.append(f"VOTE {hh}: THERE IS A DILEMMA")
    print(*answers, sep="\n")