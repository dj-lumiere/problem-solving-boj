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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        machine_code = input()
        current_position = 0
        nop_count = 0
        i = 0
        while i < len(machine_code):
            if machine_code[i].isupper():
                if current_position % 4 != 0:
                    nop_needed = 4 - (current_position % 4)
                    nop_count += nop_needed
                    current_position += nop_needed
                current_position += 1
                i += 1
                while i < len(machine_code) and machine_code[i].islower():
                    current_position += 1
                    i += 1
            else:
                i += 1
        answer = nop_count
        answers.append(answer)
    print(*answers, sep="\n")
