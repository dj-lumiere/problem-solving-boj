import re
from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from collections import deque, Counter
from datetime import datetime, time, timedelta
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from math import cos, comb, log, gcd, floor, log2, log10, log1p, pi, ceil, factorial, sin, sqrt, atan2, tau
from os import write
from random import randint, shuffle
from string import ascii_uppercase, ascii_lowercase
from sys import setrecursionlimit, stdout, stderr
from time import perf_counter_ns, sleep

digits = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
          ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
          ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], ["", "M", "MM", "MMM", "MMMM"]]

numbers = ["" for _ in range(5000)]
for i in range(5000):
    numbers[i] = digits[3][i // 1000] + digits[2][i // 100 % 10] + digits[1][i // 10 % 10] + digits[0][i % 10]
numbers_reverse = {v: i for i, v in enumerate(numbers)}

def roman_to_integer(x):
    return numbers_reverse[x]


def integer_to_roman(x):
    return numbers[x]


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    operation = "+-*/="
    answers = []
    for hh in range(1, t + 1):
        operations = []
        while s := input():
            if s is None:
                break
            operations.append(s)
        has_stack_underflowed = False
        is_out_of_range = False
        has_divided_by_zero = False
        stack = []
        for v in operations:
            match v:
                case "+":
                    if len(stack) < 2:
                        answers.append("stack underflow")
                        continue
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)
                case "-":
                    if len(stack) < 2:
                        answers.append("stack underflow")
                        continue
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "*":
                    if len(stack) < 2:
                        answers.append("stack underflow")
                        continue
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                case "/":
                    if len(stack) < 2:
                        answers.append("stack underflow")
                        continue
                    b, a = stack.pop(), stack.pop()
                    if b == 0:
                        answers.append("division by zero exception")
                        stack.append(a)
                        continue
                    stack.append(a // b)
                case "=":
                    if not stack:
                        answers.append("stack underflow")
                        continue
                    a = stack[-1]
                    if not 1 <= a < 5000:
                        answers.append("out of range exception")
                        continue
                    answers.append(integer_to_roman(a))
                case _:
                    stack.append(roman_to_integer(v))
    print(*answers, sep="\n")
