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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        K = int(input())
        student_numbers = set(int(input()) for _ in range(K))
        N = int(input())
        best_student_number = -1
        best_student_time = INF
        certificate_count = 0
        CERTIFICATE_LIMIT = 6 * 60
        for _ in range(N):
            participant_number, hours, minutes = (int(input()) for _ in range(3))
            if participant_number in student_numbers and hours >= 0 and minutes >= 0:
                total_time = hours * 60 + minutes
                if total_time <= CERTIFICATE_LIMIT:
                    certificate_count += 1
                    if total_time < best_student_time:
                        best_student_time = total_time
                        best_student_number = participant_number
        answers.append(f"{best_student_number} {certificate_count}")

    print(*answers, sep="\n")
