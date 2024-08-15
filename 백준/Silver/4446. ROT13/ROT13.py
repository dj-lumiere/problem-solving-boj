from bisect import bisect_left, bisect_right
from collections import Counter, deque
from decimal import getcontext
from itertools import combinations, product
from math import floor, log10
from sys import stdout, stderr
from fractions import Fraction

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
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
        table = {}
        for i, j in zip("aiyeou", "eouaiy"):
            table[i] = j
            table[i.upper()] = j.upper()
        for i, j in zip("bkxznhdcwgpvjqtsrlmf", "pvjqtsrlmfbkxznhdcwg"):
            table[i] = j
            table[i.upper()] = j.upper()
        sentence = input()
        if sentence is None:
            break
        answer = ""
        for i, v in enumerate(sentence):
            if v not in table:
                answer += v
            else:
                answer += table[v]
        answers.append(f"{answer}")
    print(*answers, sep="\n")