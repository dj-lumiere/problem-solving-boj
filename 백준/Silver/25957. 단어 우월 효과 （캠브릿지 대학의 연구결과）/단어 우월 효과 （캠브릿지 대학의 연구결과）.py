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
        n = int(input())
        words = [input().decode() for _ in range(n)]
        m = int(input())
        answer = [input().decode() for _ in range(m)]
        word_dict = {}
        for i, word in enumerate(words):
            if len(word) == 1:
                word_dict[word] = word
            elif len(word) == 2:
                word_dict[word] = word
            else:
                key = "".join([word[0]] + sorted(word[1:-1]) + [word[-1]])
                word_dict[key] = word
        for i, word in enumerate(answer):
            if len(word) <= 2:
                answer[i] = word_dict[word]
            else:
                key = "".join([word[0]] + sorted(word[1:-1]) + [word[-1]])
                answer[i] = word_dict[key]
        answers[hh] = f"{' '.join(answer)}"
        print(answers)