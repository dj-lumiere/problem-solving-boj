from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import cmp_to_key
from itertools import combinations, permutations, product
from math import sqrt
from sys import stdout, stderr

getcontext().prec = 30


def count_cars_and_buildings(r, c):
    cars = 0
    for i in range(2):
        for j in range(2):
            if parking_lot[r + i][c + j] == '#':
                return -1
            elif parking_lot[r + i][c + j] == 'X':
                cars += 1
    return cars


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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        R, C = map(int, input().split())
        parking_lot = [input() for _ in range(R)]
        count_spaces = [0, 0, 0, 0, 0]
        for r in range(R - 1):
            for c in range(C - 1):
                result = count_cars_and_buildings(r, c)
                if result != -1:
                    count_spaces[result] += 1
        answer = "\n".join(map(str, count_spaces))
        answers.append(f"{answer}")
    print(*answers, sep="\n")