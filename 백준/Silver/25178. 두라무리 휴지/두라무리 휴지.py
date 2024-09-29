from bisect import bisect_right
from collections import Counter, deque
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
from operator import index
from sys import stdout, stderr
from itertools import permutations

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
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
        vowels = "aeiou"
        N = int(input())
        word1 = input()
        word2 = input()
        answer = ""
        if word1[0] != word2[0] or word1[-1] != word2[-1]:
            answer = "NO"
        elif Counter(word1) != Counter(word2):
            answer = "NO"
        else:
            word1_without_vowels = "".join([ch for ch in word1 if ch not in vowels])
            word2_without_vowels = "".join([ch for ch in word2 if ch not in vowels])
            if word1_without_vowels == word2_without_vowels:
                answer = "YES"
            else:
                answer = "NO"
        answers.append(answer)
    print(*answers, sep="\n")