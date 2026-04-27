from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop, heapify
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

def get_operation_priority(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == " ":
        return 2
    return 0


def post_expression(expression):
    stack = []
    result = []
    parenthesis_stack = 0
    for i, v in enumerate(expression):
        if isinstance(v, int):
            result.append(v)
        elif v == "(":
            stack.append(v)
        elif v == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
        else:
            while (
                    stack
                    and stack[-1] != "("
                    and get_operation_priority(stack[-1]) >= get_operation_priority(v)
            ):
                result.append(stack.pop())
            stack.append(v)
    while stack:
        result.append(stack.pop())
    return result


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
    for hh in range(t):
        n = int(input())
        numbers = list(range(1, n + 1))
        result = []
        for op in product(["+", "-", " "], repeat=n - 1):
            expression = [numbers[0]]
            expression.extend(chain(*(chain(b, [a]) for a, b in zip(numbers[1:], op))))
            x = post_expression(expression)
            sub_result = []
            for v in x:
                if isinstance(v, int):
                    sub_result.append(v)
                else:
                    b, a = sub_result.pop(), sub_result.pop()
                    if v == "+":
                        sub_result.append(a + b)
                    elif v == "-":
                        sub_result.append(a - b)
                    elif v == " ":
                        sub_result.append(a * 10 + b)
            sub_result_result = sub_result[0]
            if sub_result_result == 0:
                result.append("".join(map(str, expression)))
        answer = "\n".join(sorted(result))
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")
