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
    t = int(input())
    answers = []
    for hh in range(t):
        N = int(input())
        L = [int(input()) for _ in range(N)]
        cost = 0
        for i in range(N - 1):
            min_val = min(L[i:])
            j = i + L[i:].index(min_val)
            L[i:j + 1] = L[i:j + 1][::-1]
            cost += j - i + 1
        answer = f"Case #{hh + 1}: {cost}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")