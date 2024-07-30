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
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 11092019
    for h in range(t):
        balls = [0, 1, 0, 0, 2]
        mix = input().decode()
        for i in mix:
            match i:
                case "A":
                    balls[1], balls[2] = balls[2], balls[1]
                case "B":
                    balls[1], balls[3] = balls[3], balls[1]
                case "C":
                    balls[1], balls[4] = balls[4], balls[1]
                case "D":
                    balls[2], balls[3] = balls[3], balls[2]
                case "E":
                    balls[2], balls[4] = balls[4], balls[2]
                case "F":
                    balls[3], balls[4] = balls[4], balls[3]
        answer = f"{balls.index(1)}\n{balls.index(2)}"
        answers[h] = f"{answer}"
    print(answers)