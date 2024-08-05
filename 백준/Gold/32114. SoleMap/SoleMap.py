from itertools import product
from sys import stdout, stderr
from math import log2, ceil

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep=" ", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep="\n", end="\n": stderr.write(sep.join(map(str, args)) + end)
    answers = []
    INF = 10 ** 18
    t = 1
    for hh in range(t):
        n = int(input())
        m = int(input())
        streets = [int(input()) for _ in range(n - 1)]
        car_count_difference = [0 for _ in range(n + 1)]
        answers = [0 for _ in range(n - 1)]
        for _ in range(m):
            u, v, x = int(input()), int(input()), int(input())
            car_count_difference[u] += x
            car_count_difference[v] -= x
        car_counts = [0 for _ in range(n)]
        for i, v in enumerate(car_count_difference[:-1]):
            car_counts[i] = v + car_counts[i - 1]
        for i in range(1, n):
            car_count = car_counts[i]
            quotient, modulo = divmod(car_count, streets[i - 1])
            answers[i - 1] = (quotient + 1) ** 2 * modulo + quotient ** 2 * (streets[i - 1] - modulo)
    print(*answers, sep="\n")
