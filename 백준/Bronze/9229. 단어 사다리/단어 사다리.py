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
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 10 ** 9
    for hh in range(t):
        is_correct = True
        words = []
        while True:
            current_word = input().decode()
            if current_word == "#":
                break
            words.append(current_word)
        if not words:
            break
        for i, j in zip(words, words[1:]):
            if len(i) != len(j):
                is_correct = False
                break
            if sum(i2 != j2 for i2, j2 in zip(i, j)) != 1:
                is_correct = False
                break
        answer = "Correct" if is_correct else "Incorrect"
        answers.append(f"{answer}")
    print(answers)