from collections import deque
from sys import stdout, stderr

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
        N = int(input())
        S = input()


        def is_ana_like(substring):
            if len(substring) < 3:
                return False
            if substring[0] != 'A' or substring[-1] != 'A':
                return False
            if substring.count('A') != 2 or substring.count('N') != 1:
                return False
            return True


        ana_count = 0
        for i in range(N):
            for j in range(i + 2, N):
                if is_ana_like(S[i:j + 1]):
                    ana_count += 1
        answer = ana_count
        answers.append(f"{answer}")
    print(*answers, sep="\n")