from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, cos, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for hh in range(t):
        sentence = input().decode().lower()
        words = sentence.split()
        space_count = int(input())
        word_frequencies = list(map(int, input().split()))
        title = "".join(map(lambda x: x[0].upper(), words))
        target_word = title.lower() + "\n" + sentence
        target_word_no_duplicate = []
        for i, v in enumerate(target_word):
            if not target_word_no_duplicate:
                target_word_no_duplicate.append(v)
            if target_word_no_duplicate[-1] == v:
                continue
            target_word_no_duplicate.append(v)
        word_counter = Counter(target_word_no_duplicate)
        can_be_written = True
        for i, v in enumerate(word_frequencies):
            alphabet = ascii_lowercase[i]
            letter_count = word_counter.get(alphabet, 0)
            if letter_count > v:
                can_be_written = False
                break
        if space_count < word_counter.get(" ", 0):
            can_be_written = False
        answer = title.upper() if can_be_written else "-1"
        answers.append(f"{answer}")
    print(*answers)