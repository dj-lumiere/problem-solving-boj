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
        N = int(input())
        M = int(input())
        limits = [int(input()) for _ in range(M)]
        first_round_baskets = []
        second_round_baskets = []
        for _ in range(N):
            basket = []
            while True:
                course = int(input())
                if course == -1:
                    break
                basket.append(course - 1)
            first_round_baskets.append(basket)
        for _ in range(N):
            basket = []
            while True:
                course = int(input())
                if course == -1:
                    break
                basket.append(course - 1)
            second_round_baskets.append(basket)
        first_enrollments = [set() for _ in range(M)]
        for student in range(N):
            for course in first_round_baskets[student]:
                first_enrollments[course].add(student)
        remaining_capacity_first = [limits[i] - len(first_enrollments[i]) for i in range(M)]
        for i, v in enumerate(remaining_capacity_first):
            if v < 0:
                first_enrollments[i].clear()
        second_enrollments = [set() for _ in range(M)]
        for student in range(N):
            for course in second_round_baskets[student]:
                second_enrollments[course].add(student)
        remaining_capacity_second = [remaining_capacity_first[i] - len(second_enrollments[i]) for i in range(M)]
        for i, v in enumerate(remaining_capacity_second):
            if v < 0:
                second_enrollments[i].clear()
        for i, (v1, v2) in enumerate(zip(first_enrollments, second_enrollments)):
            first_enrollments[i] = first_enrollments[i].union(v2)
        registered_courses = [set() for _ in range(N)]
        for course, students in enumerate(first_enrollments):
            for student in students:
                registered_courses[student].add(course)
        result = []
        for student in range(N):
            if registered_courses[student]:
                result.append(" ".join(map(str, sorted(c + 1 for c in registered_courses[student]))))
            else:
                result.append("망했어요")
        answer = "\n".join(result)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
