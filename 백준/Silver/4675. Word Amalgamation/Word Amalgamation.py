from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    DIAGONAL = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        dictionary = []
        while True:
            s = input()
            if s == "XXXXXX":
                break
            dictionary.append(s)
        letter_count = [sorted(Counter(i).items()) for i in dictionary]
        target = []
        while True:
            s = input()
            if s == "XXXXXX":
                break
            target.append(s)
        result = [[] for _ in target]
        for i, v in enumerate(target):
            for v1, v2 in zip(dictionary, letter_count):
                if sorted(Counter(v).items()) == v2:
                    result[i].append(v1)
        for i in range(len(target)):
            if not result[i]:
                result[i].append("NOT A VALID WORD")
            result[i].sort()
        answer = "\n******\n".join("\n".join(x) for x in result) + "\n******"
        answers.append(f"{answer}")
print(*answers, sep="\n")
