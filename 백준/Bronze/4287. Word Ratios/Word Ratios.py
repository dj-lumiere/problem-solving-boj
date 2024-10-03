from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
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
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(1, t + 1):
        def letter_shift(c1, c2):
            return (ord(c2) - ord(c1)) % 26
        def apply_shift(word, shifts):
            result = []
            for i in range(len(word)):
                new_char = chr(((ord(word[i]) - ord('a') + shifts[i]) % 26) + ord('a'))
                result.append(new_char)
            return ''.join(result)
        line = input()
        if line == '#':
            break
        word1, word2, word3 = line.split()
        shifts = [letter_shift(word1[i], word2[i]) for i in range(len(word1))]
        answer = apply_shift(word3, shifts)
        answers.append(f"{word1} {word2} {word3} {answer}")
    print(*answers, sep="\n")