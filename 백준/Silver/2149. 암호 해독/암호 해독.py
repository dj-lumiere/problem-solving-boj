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
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    for hh in range(t):
        key = input().decode()
        cyphertexts = input().decode()
        cyphertext_transpose = ""
        for i in range(len(cyphertexts) // len(key)):
            for j in range(len(key)):
                cyphertext_transpose += cyphertexts[j * (len(cyphertexts) // len(key)) + i]
        change_order = list(range(len(key)))
        change_order = sorted(change_order, key=lambda x: (key[x], x))
        answer = ""
        for i in range(len(cyphertexts) // len(key)):
            cyphertext = cyphertext_transpose[i * len(key):(i + 1) * len(key)]
            decyphertext = ["" for _ in range(len(cyphertext))]
            for i, v in enumerate(change_order):
                decyphertext[v] = cyphertext[i]
            answer += "".join(decyphertext)
        answers.append(f"{answer}")
    print(answers)