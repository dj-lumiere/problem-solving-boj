from itertools import permutations
from sys import stderr, stdout

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
    t = INF
    answers = []
    numbers = []
    for i in range(1, 9):
        for n in permutations(range(10), i):
            if n[0] == 0:
                continue
            numbers.append(int("".join(map(str, n))))
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        answer = numbers[n - 1]
        answers.append(f"{answer}")
    print(*answers, sep="\n")