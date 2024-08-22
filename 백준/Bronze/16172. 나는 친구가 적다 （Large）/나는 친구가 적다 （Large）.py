from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import stdout, stderr, setrecursionlimit
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from array import array
import re

getcontext().prec = 1000


def pattern_match(pattern, text):
    result = []
    M = len(pattern)
    N = len(text)

    longest_prefix_suffix_length = [0] * M
    j = 0
    calculate_lps_length(pattern, M, longest_prefix_suffix_length)

    i = 0
    while (N - i) >= (M - j):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            result.append(i - j + 1)
            j = longest_prefix_suffix_length[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = longest_prefix_suffix_length[j - 1]
            else:
                i += 1
    return result


def calculate_lps_length(pattern, M, lps):
    longest_prefix_suffix_length = 0

    lps[0] = 0
    i = 1

    while i < M:
        if pattern[i] == pattern[longest_prefix_suffix_length]:
            longest_prefix_suffix_length += 1
            lps[i] = longest_prefix_suffix_length
            i += 1
        else:
            if longest_prefix_suffix_length != 0:
                longest_prefix_suffix_length = lps[longest_prefix_suffix_length - 1]
            else:
                lps[i] = 0
                i += 1
                

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    losing_hand = {"R": "P", "P": "S", "S": "R"}
    for hh in range(t):
        s = "".join([v for v in input() if v.isalpha()])
        k = input()
        answer = int(bool(pattern_match(k, s)))
        answers.append(f"{answer}")
    print(*answers, sep="\n")