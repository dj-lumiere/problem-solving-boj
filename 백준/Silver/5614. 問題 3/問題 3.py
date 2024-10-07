from collections import deque, Counter
from itertools import product, chain, permutations, combinations, repeat
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt
from heapq import heappush, heappop

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    T = 1
    answers = []
    for hh in range(1, T + 1):
        n = int(input())
        order_totals = {}
        for _ in range(n):
            product_name = input()
            order_quantity = int(input())
            if product_name in order_totals:
                order_totals[product_name] += order_quantity
            else:
                order_totals[product_name] = order_quantity
        sorted_products = sorted(order_totals.keys(), key=lambda x: (len(x), x))
        for product in sorted_products:
            answers.extend((product, order_totals[product]))
    print(*answers, sep="\n")
