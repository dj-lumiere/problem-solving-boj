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
        n, m = int(input()), int(input())
        Ti = [int(input()) for _ in range(n)]
        sum_ti = [0] + Ti[:]
        for i in range(1, n + 1):
            sum_ti[i] = sum_ti[i] + sum_ti[i - 1]
        max_sum = -INF
        for i in range(n - m + 1):
            max_sum = max(max_sum, sum_ti[i + m] - sum_ti[i])
        answer = f"{max_sum}"
        answers.append(answer)
    print(*answers, sep="\n")