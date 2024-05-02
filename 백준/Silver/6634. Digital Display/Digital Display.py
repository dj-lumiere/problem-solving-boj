from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    print = lambda x: write(1, "\n\n\n".join(x + ["end"]).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    clock = {"0": ["+---+", "|   |", "|   |", "+   +", "|   |", "|   |", "+---+"],
             "1": ["    +", "    |", "    |", "    +", "    |", "    |", "    +"],
             "2": ["+---+", "    |", "    |", "+---+", "|    ", "|    ", "+---+"],
             "3": ["+---+", "    |", "    |", "+---+", "    |", "    |", "+---+"],
             "4": ["+   +", "|   |", "|   |", "+---+", "    |", "    |", "    +"],
             "5": ["+---+", "|    ", "|    ", "+---+", "    |", "    |", "+---+"],
             "6": ["+---+", "|    ", "|    ", "+---+", "|   |", "|   |", "+---+"],
             "7": ["+---+", "    |", "    |", "    +", "    |", "    |", "    +"],
             "8": ["+---+", "|   |", "|   |", "+---+", "|   |", "|   |", "+---+"],
             "9": ["+---+", "|   |", "|   |", "+---+", "    |", "    |", "+---+"],
             ":": [" ", " ", "o", " ", "o", " ", " "],}
    for h in range(t):
        pass
    while True:
        time = input().decode()
        if time == "end":
            break
        grid = [[] for _ in range(7)]
        for i in time:
            for j in range(7):
                grid[j].append(clock[i][j])
        answer = "\n".join("  ".join(x) for x in grid)
        answers.append(answer)
    print(answers)