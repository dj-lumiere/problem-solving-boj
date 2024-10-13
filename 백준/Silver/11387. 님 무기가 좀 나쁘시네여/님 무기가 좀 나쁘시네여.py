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
        def calculate_power(stats):
            atk, strn, crit_chance, crit_dmg, atk_spd = stats
            crit_chance = min(crit_chance, 100)
            combat_power = atk * (100 + strn) * (100 * (100 - crit_chance) + crit_chance * crit_dmg) * (100 + atk_spd)
            return combat_power
        crey_stats = [int(input()) for _ in range(5)]
        pabu_stats = [int(input()) for _ in range(5)]
        crey_weapon = [int(input()) for _ in range(5)]
        pabu_weapon = [int(input()) for _ in range(5)]
        crey_power = calculate_power(crey_stats)
        pabu_power = calculate_power(pabu_stats)
        crey_with_pabu_weapon = calculate_power([crey_stats[i] - crey_weapon[i] + pabu_weapon[i] for i in range(5)])
        pabu_with_crey_weapon = calculate_power([pabu_stats[i] - pabu_weapon[i] + crey_weapon[i] for i in range(5)])
        if crey_with_pabu_weapon > crey_power:
            answers.append("+")
        elif crey_with_pabu_weapon < crey_power:
            answers.append("-")
        else:
            answers.append("0")
        if pabu_with_crey_weapon > pabu_power:
            answers.append("+")
        elif pabu_with_crey_weapon < pabu_power:
            answers.append("-")
        else:
            answers.append("0")
    print(*answers, sep="\n")