from decimal import Decimal
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
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        lst = [int(input()) for _ in range(n)]
        if n == 0:
            answer = "0"
        else:
            max_len = 1
            current_len = 1
            for i in range(1, n):
                if lst[i] > lst[i - 1]:
                    current_len += 1
                    if current_len > max_len:
                        max_len = current_len
                else:
                    current_len = 1
            answer = f"{max_len}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")