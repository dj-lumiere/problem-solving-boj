from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for hh in range(t):
        words = list(input().decode().strip().split())
        animal_sounds = {}
        while True:
            sentence = input().decode().strip().split()
            if sentence == ["what", "does", "the", "fox", "say?"]:
                break
            animal, _, sound = sentence
            animal_sounds[animal] = sound
        answer = [i for i in words if i not in animal_sounds.values()]
        answers[hh] = " ".join(answer)
    print(answers)