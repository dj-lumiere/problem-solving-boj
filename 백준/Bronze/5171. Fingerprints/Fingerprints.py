from array import array
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
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

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
    x = 1
    answers = []
    for hh in range(1, x + 1):
        n = int(input())
        K = int(input())
        database = []
        for i in range(n):
            fingerprint = []
            for _ in range(5):
                fingerprint.append(input())
            database.append(fingerprint)
        crimes = []
        for i in range(K):
            crime_fingerprint = []
            for _ in range(5):
                crime_fingerprint.append(input())
            crimes.append(crime_fingerprint)
        for case_idx in range(K):
            crime = crimes[case_idx]
            min_distance = INF
            best_matches = []
            for db_idx in range(n):
                db_fingerprint = database[db_idx]
                distance = 0
                for row in range(5):
                    for col in range(5):
                        if db_fingerprint[row][col] != crime[row][col]:
                            distance += 1
                if distance < min_distance:
                    min_distance = distance
                    best_matches = [db_idx + 1]
                elif distance == min_distance:
                    best_matches.append(db_idx + 1)
            answers.append(f"Data Set {case_idx + 1}:\n"+" ".join(map(str, sorted(best_matches)))+"\n")
    print(*answers, sep="\n")