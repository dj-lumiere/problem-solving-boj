from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal

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
        N, M = int(input()), int(input())
        results = [input() for _ in range(M)]
        snupti_posible = "YES"
        scales = [set() for _ in range(N)]
        for result in results:
            for i in range(N):
                scales[i].add(result[i])
        for i in range(N):
            for j in range(i + 1, N):
                if scales[i].intersection(scales[j]):
                    snupti_posible = "NO"
                    break
            if snupti_posible == "NO":
                break
        sorted_results = ["".join(sorted(scale)) for scale in scales]
        if snupti_posible == "YES" and sorted(results) == sorted("".join(s) for s in product(*sorted_results)):
            answer = "YES\n" + "\n".join(sorted_results)
        else:
            answer = "NO"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
