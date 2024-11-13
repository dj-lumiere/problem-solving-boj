from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    answers = []
    for hh in range(t):
        line = input()
        eq = line.split('=')
        left = eq[0].split('+')
        M1 = left[0].strip()
        M2 = left[1].strip()
        M3 = eq[1].strip()
        eprint(M1, M2, M3)
        counts1 = {'C': 0, 'H': 0, 'O': 0}
        i = 0
        while i < len(M1):
            atom = M1[i]
            i += 1
            num = ''
            while i < len(M1) and M1[i].isdigit():
                num += M1[i]
                i += 1
            counts1[atom] += int(num) if num else 1
        counts2 = {'C': 0, 'H': 0, 'O': 0}
        i = 0
        while i < len(M2):
            atom = M2[i]
            i += 1
            num = ''
            while i < len(M2) and M2[i].isdigit():
                num += M2[i]
                i += 1
            counts2[atom] += int(num) if num else 1
        counts3 = {'C': 0, 'H': 0, 'O': 0}
        i = 0
        while i < len(M3):
            atom = M3[i]
            i += 1
            num = ''
            while i < len(M3) and M3[i].isdigit():
                num += M3[i]
                i += 1
            counts3[atom] += int(num) if num else 1
        found = False
        for X1 in range(1, 11):
            for X2 in range(1, 11):
                for X3 in range(1, 11):
                    C = X1 * counts1['C'] + X2 * counts2['C']
                    H = X1 * counts1['H'] + X2 * counts2['H']
                    O = X1 * counts1['O'] + X2 * counts2['O']
                    if C == X3 * counts3['C'] and H == X3 * counts3['H'] and O == X3 * counts3['O']:
                        answer = f"{X1} {X2} {X3}"
                        answers.append(f"{answer}")
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            answer = "0 0 0"
            answers.append(f"{answer}")
    print(*answers)
