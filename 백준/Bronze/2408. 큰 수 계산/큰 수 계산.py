from collections import deque
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
from sys import stdout, stderr
from itertools import permutations

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())


        def get_operation_priority(operator):
            if operator == "+" or operator == "-":
                return 1
            if operator == "*" or operator == "/":
                return 2
            return 0


        expression = [int(input())]
        for _ in range(N - 1):
            expression.extend([input(), int(input())])
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
                while (stack and stack[-1] != "(" and get_operation_priority(stack[-1]) >= get_operation_priority(v)):
                    result.append(stack.pop())
                stack.append(v)
        while stack:
            result.append(stack.pop())
        for i in result:
            if isinstance(i, int):
                stack.append(i)
                continue
            if i == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            if i == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            if i == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            if i == "/":
                b, a = stack.pop(), stack.pop()
                q, r = divmod(abs(a), abs(b))
                if a > 0 and b < 0:
                    if r != 0:
                        q = -q - 1
                    else:
                        q = -q
                if a < 0 and b > 0:
                    if r != 0:
                        q = -q - 1
                    else:
                        q = -q
                stack.append(q)
        answer = stack.pop()
        answers.append(f"{answer}")
    print(*answers, sep="\n")