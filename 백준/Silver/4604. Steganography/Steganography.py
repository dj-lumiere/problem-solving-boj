from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, \
    groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re
from datetime import datetime, time, timedelta

getcontext().prec = 1000

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = INF
    answers = []
    binary_to_char = {'00000': ' ', '00001': 'A', '00010': 'B', '00011': 'C', '00100': 'D', '00101': 'E', '00110': 'F',
        '00111': 'G', '01000': 'H', '01001': 'I', '01010': 'J', '01011': 'K', '01100': 'L', '01101': 'M', '01110': 'N',
        '01111': 'O', '10000': 'P', '10001': 'Q', '10010': 'R', '10011': 'S', '10100': 'T', '10101': 'U', '10110': 'V',
        '10111': 'W', '11000': 'X', '11001': 'Y', '11010': 'Z', '11011': "'", '11100': ',', '11101': '-', '11110': '.',
        '11111': '?'}
    for hh in range(1, t + 1):
        sentences = []
        while True:
            s = input()
            if s == "#":
                break
            if s == "*":
                break
            sentences.append(s)
        if not sentences:
            break
        spaces = []
        for s in sentences:
            for i, v in groupby(s):
                if i == " ":
                    spaces.append(len(list(v)))
        bits = ""
        for v in spaces:
            if v % 2 == 0:
                bits += "1"
            else:
                bits += "0"
        while len(bits) % 5 != 0:
            bits += "0"
        message = ""
        for i in range(0, len(bits), 5):
            chunk = bits[i:i + 5]
            if chunk in binary_to_char:
                message += binary_to_char[chunk]
        answer = message
        answers.append(f"{answer}")
print(*answers, sep="\n")
