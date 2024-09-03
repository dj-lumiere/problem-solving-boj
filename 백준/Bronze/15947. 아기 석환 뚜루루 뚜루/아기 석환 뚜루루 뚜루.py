from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import product, chain, permutations, combinations, repeat
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
    POSSIBLE_DIRECTION = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    BETWEEN = [((0, 1), (0, -1)), ((-1, 0), (1, 0))]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        s = ['baby', 'sukhwan', 'tu', 'tu', 'very', 'cute', 'tu', 'tu', 'in', 'bed', 'tu', 'tu', 'baby', 'sukhwan']
        ru_count = lambda x: [0, 0, 2 + x, 1 + x, 0, 0, 2 + x, 1 + x, 0, 0, 2 + x, 1 + x, 0, 0]
        completed_phrase, remainder = divmod(n - 1, len(s))
        ru_count_current = ru_count(completed_phrase)
        answer = ""
        if ru_count_current[remainder] == 0:
            answer = s[remainder]
        elif ru_count_current[remainder] < 5:
            answer = s[remainder] + "ru" * ru_count_current[remainder]
        else:
            answer = f"{s[remainder]}+ru*{ru_count_current[remainder]}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
