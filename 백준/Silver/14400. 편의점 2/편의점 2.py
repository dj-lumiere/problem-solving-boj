from sys import stdout, stderr

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
    for hh in range(t):
        n = int(input())
        x_dots = []
        y_dots = []
        for _ in range(n):
            x, y = (int(input()) for _ in range(2))
            x_dots.append(x * 2)
            y_dots.append(y * 2)
        x_dots.sort()
        y_dots.sort()
        x_middle = x_dots[n // 2] if n % 2 == 1 else (x_dots[n // 2] + x_dots[n // 2 - 1]) // 2
        y_middle = y_dots[n // 2] if n % 2 == 1 else (y_dots[n // 2] + y_dots[n // 2 - 1]) // 2
        distance = (sum(abs(i - x_middle) for i in x_dots) + sum(abs(i - y_middle) for i in y_dots)) // 2
        answer = distance
        answers.append(f"{answer}")
    print(*answers, sep="\n")
