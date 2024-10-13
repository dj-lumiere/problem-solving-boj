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
        A = int(input())
        B = int(input())
        C = int(input())
        general_menu = {}
        special_menu = {}
        service_menu = set()
        for i in range(A):
            name = input()
            price = int(input())
            general_menu[name] = price
        for i in range(B):
            name = input()
            price = int(input())
            special_menu[name] = price
        for i in range(C):
            name = input()
            service_menu.add(name)
        N = int(input())
        ordered_general_total = 0
        ordered_special_total = 0
        service_ordered = False
        invalid_order = False
        for i in range(N):
            item_name = input()
            if item_name in general_menu:
                ordered_general_total += general_menu[item_name]
            elif item_name in special_menu:
                ordered_special_total += special_menu[item_name]
            elif item_name in service_menu:
                if service_ordered:
                    invalid_order = True
                else:
                    service_ordered = True
            else:
                invalid_order = True
        if invalid_order:
            answers.append("No")
        else:
            total_price = ordered_general_total + ordered_special_total
            if service_ordered and total_price < 50000:
                answers.append("No")
            elif ordered_special_total > 0 and ordered_general_total < 20000:
                answers.append("No")
            else:
                answers.append("Okay")
    print(*answers, sep="\n")