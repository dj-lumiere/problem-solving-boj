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
        N = int(input())
        g = int(input())
        ratings = []
        for i in range(N):
            ratings.append(int(input()))
        played_songs = []
        for _ in range(g):
            max_index = 0
            for i in range(1, N):
                if ratings[i] > ratings[max_index]:
                    max_index = i
                elif ratings[i] == ratings[max_index] and i < max_index:
                    max_index = i
            played_songs.append(max_index + 1)
            played_rating = ratings[max_index]
            ratings[max_index] = 0
            if N > 1:
                distributed_points = played_rating // (N - 1)
                extra_points = played_rating % (N - 1)
                for i in range(N):
                    if i != max_index:
                        ratings[i] += distributed_points
                i = 0
                while extra_points > 0:
                    if i != max_index:
                        ratings[i] += 1
                        extra_points -= 1
                    i += 1
        answers.extend(played_songs)
    print(*answers, sep="\n")
