from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": write(1, (sep.join(map(str, args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": write(2, (sep.join(map(str, args)) + end).encode())
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    judge_sequence = [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15), (0, 4, 8, 12), (1, 5, 9, 13),
                      (2, 6, 10, 14), (3, 7, 11, 15), (0, 5, 10, 15), (3, 6, 9, 12)]
    for hh in range(t):
        game_status = ""
        grid = []
        for _ in range(4):
            grid.extend(list(input().decode()))
        has_complete_x = any(all(grid[i] in "XT" for i in j) for j in judge_sequence)
        has_complete_o = any(all(grid[i] in "OT" for i in j) for j in judge_sequence)
        has_complete_board = all(i != "." for i in grid)
        if has_complete_o and has_complete_x:
            game_status = "Draw"
        elif has_complete_o:
            game_status = "O won"
        elif has_complete_x:
            game_status = "X won"
        elif has_complete_board:
            game_status = "Draw"
        else:
            game_status = "Game has not completed"
        answer = f"Case #{hh + 1}: {game_status}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
