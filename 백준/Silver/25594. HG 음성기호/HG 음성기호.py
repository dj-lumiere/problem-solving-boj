from array import array
from base64 import b64decode, b64encode
from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, time, timedelta
from sys import setrecursionlimit, stdout, stderr
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import cos, comb, log, gcd, floor, log2, log10, pi, ceil, factorial, sin, sqrt, atan2, tau
from heapq import heapify, heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest, chain, repeat, groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = 1
    answers = []
    for hh in range(1, x + 1):
        hg_map = {
            'aespa'   : 'a', 'baekjoon': 'b', 'cau': 'c', 'debug': 'd', 'edge': 'e', 'firefox': 'f',
            'golang'  : 'g', 'haegang': 'h', 'iu': 'i', 'java': 'j', 'kotlin': 'k', 'lol': 'l',
            'mips'    : 'm', 'null': 'n', 'os': 'o', 'python': 'p', 'query': 'q', 'roka': 'r',
            'solvedac': 's', 'tod': 't', 'unix': 'u', 'virus': 'v', 'whale': 'w', 'xcode': 'x',
            'yahoo'   : 'y', 'zebra': 'z'
        }
        S = input()
        original_word = []
        current_pos = 0
        is_valid = True
        while current_pos < len(S):
            matched = False
            for phonetic, letter in hg_map.items():
                if S[current_pos:current_pos + len(phonetic)] == phonetic:
                    original_word.append(letter)
                    current_pos += len(phonetic)
                    matched = True
                    break
            if not matched:
                is_valid = False
                break
        if is_valid:
            answers.append("It's HG!")
            answers.append("".join(original_word))
        else:
            answers.append("ERROR!")
    print(*answers, sep="\n")