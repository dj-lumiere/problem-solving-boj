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
        for i in range(n):
            location = input()
            data = input()
            bobcat_count = 0
            coyote_count = 0
            mountain_lion_count = 0
            wolf_count = 0
            for char in data:
                if char == 'B':
                    bobcat_count += 2
                elif char == 'C':
                    coyote_count += 1
                elif char == 'M':
                    mountain_lion_count += 4
                elif char == 'W':
                    wolf_count += 3
            species = {
                "Bobcat": bobcat_count,
                "Coyote": coyote_count,
                "Mountain Lion": mountain_lion_count,
                "Wolf": wolf_count
            }
            max_value = max(species.values())
            dominant_species = [key for key, value in species.items() if value == max_value]
            if len(dominant_species) > 1:
                answers.append(f"{location}: There is no dominant species")
            else:
                answers.append(f"{location}: The {dominant_species[0]} is the dominant species")
    print(*answers, sep="\n")