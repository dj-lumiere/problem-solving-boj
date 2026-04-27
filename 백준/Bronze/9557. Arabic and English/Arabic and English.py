from bisect import bisect_left
from string import ascii_lowercase
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
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        n = int(input())
        words = [input().decode() for _ in range(n)]
        if all([all(i == "#" for i in word) for word in words]):
            pass
        elif all([all(i in ascii_lowercase for i in word) for word in words]):
            pass
        else:
            words_before = []
            words_after = []
            found_alphabet = False
            alphabet_word = []
            for word in words:
                if all(i in ascii_lowercase for i in word):
                    found_alphabet = True
                    alphabet_word.append(word)
                    continue
                if not found_alphabet:
                    words_before.append(word)
                else:
                    words_after.append(word)
            words = words_after + alphabet_word + words_before
        answers[h] = " ".join(words)
    print(answers)