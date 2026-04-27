from sys import stderr, stdout
from string import ascii_uppercase
from itertools import combinations

def find_all_comb(s):
    result = []
    for i, j in combinations(range(len(s)), 2):
        if s[i] == s[j] != "X":
            result.append((i, j))
    return result

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 998244353
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        k = int(input())
        s = input()
        len_min = len(s)
        for a, b in find_all_comb(s):
            s2 = s[:a] + s[b+1:]
            len_min = min(len_min, len(s2))
            for c, d in find_all_comb(s2):
                s3 = s2[:c] + s2[d+1:]
                len_min = min(len_min, len(s3))
        answers.append(len_min)
    print(*answers, sep="\n")