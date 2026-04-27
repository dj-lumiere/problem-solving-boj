from bisect import bisect_left
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


    def find_midpoint(start, end):
        start_row, start_col = divmod(start - 1, 3)
        end_row, end_col = divmod(end - 1, 3)
        if start != end and not (((start_row ^ end_row) | (start_col ^ end_col)) & 1):
            midpoint_row = (start_row + end_row) // 2
            midpoint_col = (start_col + end_col) // 2
            return midpoint_row * 3 + midpoint_col + 1
        return None


    def find_patterns(current_num, remaining_steps, total_steps, grid_size, current_pattern, all_patterns):
        if remaining_steps == 0:
            all_patterns.append("".join(map(str, current_pattern)))
            return

        for next_num in range(1, grid_size + 1):
            midpoint = find_midpoint(current_num, next_num)
            if next_num not in current_pattern and (
                    remaining_steps == total_steps or not midpoint or midpoint in current_pattern):
                current_pattern.append(next_num)
                find_patterns(next_num, remaining_steps - 1, total_steps, grid_size, current_pattern, all_patterns)
                current_pattern.pop()


    def generate_patterns(patterns, grid_size, min_length):
        all_patterns = []
        for length in range(min_length, grid_size + 1):
            find_patterns(1, length, length, grid_size, [], all_patterns)
        patterns.extend(all_patterns)


    all_patterns = []
    generate_patterns(all_patterns, 9, 3)

    for hh in range(t):
        l = int(input())
        x = "".join([input().decode() for _ in range(l)])
        answer = "YES" if x in all_patterns else "NO"
        answers.append(f"{answer}")
    print(answers)