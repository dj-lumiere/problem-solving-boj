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
        encoded_message_1 = input()
        encoded_message_2 = input()
        N = len(encoded_message_1) // 2 
        recovered_key = []
        SPACE_BYTE = 32
        message_1_bytes = []
        message_2_bytes = []
        for i in range(0, len(encoded_message_1), 2):
            byte = int(encoded_message_1[i:i + 2], 16)
            message_1_bytes.append(byte)
        for i in range(0, len(encoded_message_2), 2):
            byte = int(encoded_message_2[i:i + 2], 16)
            message_2_bytes.append(byte)
        original_message = []
        recovered_key.append(message_2_bytes[0] ^ SPACE_BYTE)
        for i, j in zip(message_2_bytes[1:], message_1_bytes):
            original_message.append(j ^ recovered_key[-1])
            recovered_key.append(i ^ original_message[-1])
        answers.append(''.join(map(lambda x: f"{x:02X}", recovered_key)))
    print(*answers, sep="\n")
