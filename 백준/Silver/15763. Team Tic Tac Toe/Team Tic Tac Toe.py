from bisect import bisect_left
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    for hh in range(t):
        answer1 = 0
        answer2 = 0
        grid = list(list(input().decode()) for _ in range(3))
        possible_alphabets = set()
        for r, c in product(range(3), repeat=2):
            possible_alphabets.add(grid[r][c])
        for i in possible_alphabets:
            check = [[grid[y][x] == i for x in range(3)] for y in range(3)]
            is_winner = False
            for x in range(3):
                if all(check[y][x] for y in range(3)):
                    is_winner = True
            for y in range(3):
                if all(check[y][x] for x in range(3)):
                    is_winner = True
            if all(check[x][x] for x in range(3)):
                is_winner = True
            if all(check[2 - x][x] for x in range(3)):
                is_winner = True
            if is_winner:
                answer1 += 1
        for i in combinations(possible_alphabets, 2):
            check = [[grid[y][x] in i for x in range(3)] for y in range(3)]
            is_winner = False
            for x in range(3):
                if all(check[y][x] for y in range(3)) and len(set([grid[y][x] for y in range(3)])) == 2:
                    is_winner = True
            for y in range(3):
                if all(check[y][x] for x in range(3)) and len(set([grid[y][x] for x in range(3)])) == 2:
                    is_winner = True
            if all(check[x][x] for x in range(3)) and len(set([grid[x][x] for x in range(3)])) == 2:
                is_winner = True
            if all(check[2 - x][x] for x in range(3)) and len(set([grid[2 - x][x] for x in range(3)])) == 2:
                is_winner = True
            if is_winner:
                answer2 += 1
        answer = f"{answer1}\n{answer2}"
        answers.append(f"{answer}")
    print(answers)