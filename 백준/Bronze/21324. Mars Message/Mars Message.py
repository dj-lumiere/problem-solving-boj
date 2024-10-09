from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from inspect import stack
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

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
    t = 1
    answers = []
    angle_to_hex = {}
    for i in range(16):
        lower_bound = i * 22.5
        upper_bound = (i + 1) * 22.5
        angle_to_hex[(lower_bound, upper_bound)] = format(i, 'x')
    for hh in range(1, t + 1):
        n = int(input())
        angles = []
        for i in range(n):
            angle = float(input())
            angles.append(angle)
        message = ""
        for i in range(0, n, 2):
            first_angle = angles[i]
            second_angle = angles[i + 1]
            for bounds, hex_digit in angle_to_hex.items():
                if bounds[0] <= first_angle < bounds[1]:
                    first_hex_digit = hex_digit
                    break
            for bounds, hex_digit in angle_to_hex.items():
                if bounds[0] <= second_angle < bounds[1]:
                    second_hex_digit = hex_digit
                    break
            hex_value = first_hex_digit + second_hex_digit
            ascii_value = int(hex_value, 16)
            message += chr(ascii_value)
        answers.append(message)
    print(*answers, sep="\n")