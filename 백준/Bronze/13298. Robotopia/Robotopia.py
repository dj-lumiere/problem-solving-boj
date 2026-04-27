from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
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
from datetime import datetime, time, timedelta

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).strip().encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    answers = ["" for _ in range(0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    for hh in range(t):
        l1, a1, l2, a2, lt, at = [int(input()) for _ in range(6)]
        answer = "?"
        d = l1 * a2 - a1 * l2
        if d == 0:
            answer = "?"
        else:
            answer1 = Fraction(a2 * lt - l2 * at, d)
            answer2 = Fraction(l1 * at - a1 * lt, d)
            if answer1.denominator != 1 or answer2.denominator != 1 or answer1 <= 0 or answer2 <= 0:
                answer = "?"
            else:
                answer = f"{int(answer1)} {int(answer2)}"
        if answer == "?":
            answer_count = 0
            for t1 in range(1, 20001):
                leg_t2, leg_remainder = divmod(lt - l1 * t1, l2)
                arm_t2, arm_remainder = divmod(at - a1 * t1, a2)
                if leg_remainder != 0 or arm_remainder != 0:
                    continue
                if leg_t2 != arm_t2:
                    continue
                if leg_t2 <= 0:
                    continue
                if answer_count > 0:
                    answer = "?"
                    break
                answer = f"{t1} {leg_t2}"
                answer_count += 1
        answers.append(f"{answer}")
    print(answers)