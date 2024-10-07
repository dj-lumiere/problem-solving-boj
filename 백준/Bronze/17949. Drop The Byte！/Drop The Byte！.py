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
        hex_string = input()

        N = int(input())
        formats = []
        for i in range(N):
            formats.append(input())
        format_sizes = {
            "char": 1,
            "int": 4,
            "long_long": 8
        }
        current_position = 0
        result = []
        for format_type in formats:
            byte_size = format_sizes[format_type]
            hex_digit_count = byte_size * 2
            hex_value = hex_string[current_position:current_position + hex_digit_count]
            decimal_value = int(hex_value, 16)
            result.append(str(decimal_value))
            current_position += hex_digit_count
        answers.extend(result)
    print(*answers, sep="\n")
