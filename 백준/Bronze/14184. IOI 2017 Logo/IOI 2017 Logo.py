from bisect import bisect_left, bisect_right
from collections import deque, Counter
from heapq import heappop, heappush
from itertools import product, chain, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter

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
    t = INF
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        if n == 0:
            break
        votes = [0 for _ in range(10 ** 6 + 1)]
        first_votes = [0 for _ in range(10 ** 6 + 1)]
        second_votes = [0 for _ in range(10 ** 6 + 1)]
        for _ in range(n):
            v = int(input())
            for i in range(v):
                a = int(input())
                votes[a] += 3 - i
                if i == 0:
                    first_votes[a] += 1
                if i == 1:
                    second_votes[a] += 1
        max_votes = max(votes)
        max_first_votes = max(v2 for i, (v1, v2, v3) in enumerate(zip(votes, first_votes, second_votes)) if
                                    v1 == max_votes)
        max_second_votes = max(v3 for i, (v1, v2, v3) in enumerate(zip(votes, first_votes, second_votes)) if
                                    v1 == max_votes and v2 == max_first_votes)
        answer = " ".join(map(str, (i for i, (v1, v2, v3) in enumerate(zip(votes, first_votes, second_votes)) if
                                    v1 == max_votes and v2 == max_first_votes and v3 == max_second_votes)))
        answers.append(f"{answer}")
    print(*answers, sep="\n")
