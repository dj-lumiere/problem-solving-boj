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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        original_word = input()
        N = int(input())
        max_ratio = -1
        selected_word = "No Jam"
        for _ in range(N):
            dict_word = input()
            g = int(input())
            j = 0
            can_be_made = False
            for i, char in enumerate(dict_word):
                if j == len(original_word):
                    can_be_made = True
                    break
                if original_word[j] == char:
                    j += 1
                    continue
            else:
                if j == len(original_word):
                    can_be_made = True
            if can_be_made:
                added_chars = len(dict_word) - len(original_word)
                if added_chars > 0:
                    ratio = g / added_chars
                    if ratio > max_ratio:
                        max_ratio = ratio
                        selected_word = dict_word
        answers.append(selected_word)
    print(*answers, sep="\n")