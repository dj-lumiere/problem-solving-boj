from time import perf_counter_ns, sleep
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, ("sep".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        word = input().decode()
        is_vowel = [+(i in "aeiou") for i in word]
        if is_vowel == [i & 1 for i in range(len(word))] or is_vowel == [1 - (i & 1) for i in range(len(word))]:
            answer = 1
        else:
            answer = 0
        answers[h] = f"{answer}"
    print(answers)