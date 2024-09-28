from collections import deque
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
from sys import stdout, stderr
from itertools import permutations

getcontext().prec = 30

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
        def rotate_90_clockwise(matrix):
            N = len(matrix)
            return [[matrix[N - j - 1][i] for j in range(N)] for i in range(N)]
        def rotate_90_counterclockwise(matrix):
            N = len(matrix)
            return [[matrix[j][N - i - 1] for j in range(N)] for i in range(N)]
        def count_differences(matrix1, matrix2):
            N = len(matrix1)
            return sum(matrix1[i][j] != matrix2[i][j] for i in range(N) for j in range(N))
        N = int(input())
        S = [list(input()) for _ in range(N)]
        T = [list(input()) for _ in range(N)]
        min_moves = count_differences(S, T)
        S_rotated_90 = rotate_90_clockwise(S)
        min_moves = min(min_moves, count_differences(S_rotated_90, T) + 1)
        S_rotated_90_counter = rotate_90_counterclockwise(S)
        min_moves = min(min_moves, count_differences(S_rotated_90_counter, T) + 1)
        S_rotated_180 = rotate_90_clockwise(S_rotated_90)
        min_moves = min(min_moves, count_differences(S_rotated_180, T) + 2)
        answers.append(f"{min_moves}")
    print(*answers, sep="\n")