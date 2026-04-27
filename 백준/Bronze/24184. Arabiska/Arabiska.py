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
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        n = int(input())
        words = [input().decode() for _ in range(n)]
        result = []
        for i, word in enumerate(words):
            new_word = []
            for j, letter in enumerate(word):
                new_word.append(letter)
                if j + 2 >= len(word):
                    continue
                if letter in "aeiouy" and (word[j + 1] not in "aeiouy" and word[j + 2] not in "aeiouy"):
                    new_word.pop()
            result.append("".join(reversed(new_word)))
        result.reverse()
        answer = " ".join(result)
        answers.append(f"{answer}")
    print(answers)