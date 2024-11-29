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
        if n == 0:
            answer = "0 0"
        else:
            A = [int(input()) for _ in range(n)]
            max_len = 1
            max_sum = A[0]
            current_len = 1
            current_sum = A[0]
            for i in range(1, n):
                if A[i] >= A[i - 1]:
                    current_len += 1
                    current_sum += A[i]
                else:
                    if current_len > max_len:
                        max_len = current_len
                        max_sum = current_sum
                    current_len = 1
                    current_sum = A[i]
            if current_len > max_len:
                max_len = current_len
                max_sum = current_sum
            answer = f"{max_len} {max_sum}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")