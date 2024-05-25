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

def digit_length(target: int) -> int:
    return floor(log10(target)) + 1


def find_ith_digit(end: int, digit_pos: int) -> int:
    return (end // (10 ** (digit_pos - 1))) % 10


def find_count(end: int, digit_pos: int, target: int) -> int:
    digit = find_ith_digit(end, digit_pos)
    result = end // (10**digit_pos) * (10 ** (digit_pos - 1))
    if target < digit:
        result += 10 ** (digit_pos - 1)
    elif target == digit:
        result += end % (10 ** (digit_pos - 1)) + 1
    return result


def number_frequency(end: int):
    num_list = [0 for i in range(10)]
    if end == 0:
        return num_list
    digit = digit_length(end)
    for i, j in product(range(1, digit + 1), range(10)):
        num_list[j] += find_count(end, i, j)
    for i in range(digit):
        num_list[0] -= 10**i
    return num_list

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
        n = int(input()) - 1
        answer = 0
        start = 0
        end = 10**9+1
        while start+1<end:
            mid = (start+end)//2
            digit_counts = number_frequency(mid)
            if sum(digit_counts) > n:
                end = mid
            else:
                start = mid
        answer = str(start+1)[n-sum(number_frequency(start))]
        answers.append(f"{answer}")
    print(answers)