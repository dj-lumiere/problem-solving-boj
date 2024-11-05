from collections import deque
from heapq import heappop, heappush
from itertools import product, permutations
from sys import stderr, stdout


def array_to_number(array):
    return sum(v << (i << 2) for i, v in enumerate(array))


def number_to_array(n, number):
    return [number >> (i << 2) & 15 for i in range(n)]


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    for hh in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        m = int(input())
        ops = [(int(input()) - 1, int(input()) - 1, int(input())) for _ in range(m)]
        queue = [(0, array_to_number(a))]
        min_cost = {array_to_number(i): INF for i in permutations(a)}
        min_cost[array_to_number(a)] = 0
        answer = INF
        while queue:
            cost, array = heappop(queue)
            if cost > min_cost[array]:
                continue
            for l, r, c in ops:
                next_array = number_to_array(n, array)
                next_array[l], next_array[r] = next_array[r], next_array[l]
                next_cost = cost + c
                next_number = array_to_number(next_array)
                if next_cost >= min_cost[next_number]:
                    continue
                min_cost[next_number] = min(min_cost[next_number], next_cost)
                heappush(queue, (next_cost, next_number))
        answer = min_cost[array_to_number(sorted(a))]
        if answer == INF:
            answer = -1
        answers.append(answer)
    print(*answers, sep="\n")
