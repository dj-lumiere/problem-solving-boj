from collections import deque, Counter
from itertools import product, chain, permutations, combinations
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt

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
        encrypted_message = input()
        conjectured_message = input()


        def can_be_encrypted_form(enc_msg, conj_msg):
            enc_counter = Counter(enc_msg)
            conj_counter = Counter(conj_msg)
            return sorted(enc_counter.values()) == sorted(conj_counter.values())


        if can_be_encrypted_form(encrypted_message, conjectured_message):
            answers.append("YES")
        else:
            answers.append("NO")
    print(*answers, sep="\n")
