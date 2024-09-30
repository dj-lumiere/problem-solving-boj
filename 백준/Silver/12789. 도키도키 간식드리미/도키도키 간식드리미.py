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
        n = int(input())
        students = [int(input()) for _ in range(n)]
        stack = []
        expected_number = 1
        for student in students:
            while stack and stack[-1] == expected_number:
                stack.pop()
                expected_number += 1
            if student == expected_number:
                expected_number += 1
            else:
                stack.append(student)
        while stack and stack[-1] == expected_number:
            stack.pop()
            expected_number += 1
        if expected_number == n + 1:
            answer = "Nice"
        else:
            answer = "Sad"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
