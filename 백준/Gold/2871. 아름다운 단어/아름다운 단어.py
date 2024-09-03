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
        s = input()
        taken = [False for _ in range(n)]
        turns = 0
        alphabets = [deque() for _ in range(26)]
        for i, v in enumerate(s):
            v2 = ord(v) - ord("a")
            alphabets[v2].append(i)
        sanggeun = []
        heewon = []
        while turns < n // 2:
            sanggeun_ptr = -1
            letter = ""
            for i, v in enumerate(alphabets):
                if not v:
                    continue
                v2 = v.pop()
                if sanggeun_ptr < v2:
                    sanggeun_ptr = v2
                    letter = i
                v.append(v2)
            alphabets[letter].pop()
            sanggeun.append(s[sanggeun_ptr])
            taken[sanggeun_ptr] = True
            heewon_ptr = 0
            for i, v in enumerate(alphabets):
                if not v:
                    continue
                v2 = v.pop()
                heewon_ptr = v2
                heewon.append(s[v2])
                taken[v2] = True
                break
            turns += 1
        heewon_win = heewon < sanggeun
        answer = f"{'DA' if heewon_win else 'NE'}\n{''.join(heewon)}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
