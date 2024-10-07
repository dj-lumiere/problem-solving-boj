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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        K = int(input())  # number of meals
        meal_prices = [int(input()) for _ in range(K)]
        X = int(input())
        menu_items = [int(input()) for _ in range(4)]
        T = int(input())
        tray_items = [int(input()) for _ in range(T)]
        total_cost = 0
        menu_count = 0
        meal_count = [0] * K
        for meal in tray_items:
            meal_count[meal - 1] += 1
        while max(meal_count[meal - 1] for meal in menu_items) > 0:
            subtotal = 0
            sub_added = set()
            for meal in menu_items:
                if meal_count[meal - 1] <= 0:
                    continue
                meal_count[meal - 1] -= 1
                subtotal += meal_prices[meal - 1]
                sub_added.add(meal - 1)
            if subtotal < X:
                for i in sub_added:
                    meal_count[i] += 1
                break
            total_cost += X
            menu_count += 1
        for i in range(K):
            if meal_count[i] > 0:
                total_cost += meal_prices[i] * meal_count[i]
        answers.append(total_cost)
    print(*answers, sep="\n")
