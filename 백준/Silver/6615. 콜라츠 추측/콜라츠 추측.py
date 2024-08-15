from bisect import bisect_left, bisect_right
from collections import Counter, deque
from decimal import getcontext
from itertools import combinations, product
from math import floor, log10
from sys import stdout, stderr
from fractions import Fraction

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(t):
        n, m = int(input()), int(input())
        if n == m == 0:
            break
        next_n, next_m = n, m
        n_path = [next_n]
        m_path = [next_m]
        while True:
            if next_n == 1:
                break
            next_n = next_n // 2 if next_n % 2 == 0 else 3 * next_n + 1
            n_path.append(next_n)
        while True:
            if next_m == 1:
                break
            next_m = next_m // 2 if next_m % 2 == 0 else 3 * next_m + 1
            m_path.append(next_m)
        n_step = 0
        m_step = 0
        intersect = 0
        for i, v in enumerate(n_path):
            if v in m_path:
                n_step = i
                m_step = m_path.index(v)
                intersect = v
                break
        answer = f"{n} needs {n_step} steps, {m} needs {m_step} steps, they meet at {intersect}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")