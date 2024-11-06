from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        dots = [(int(input()), int(input())) for _ in range(n)]
        s = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(dots, dots[1:] + [dots[0]]))
        integral_x_sq = sum(
            (x2 ** 3 + x2 ** 2 * x1 + x2 * x1 ** 2 + x1 ** 3) * (y2 - y1) for (x1, y1), (x2, y2) in
            zip(dots, dots[1:] + [dots[0]]))
        integral_y_sq = -sum(
            (y2 ** 3 + y2 ** 2 * y1 + y2 * y1 ** 2 + y1 ** 3) * (x2 - x1) for (x1, y1), (x2, y2) in
            zip(dots, dots[1:] + [dots[0]]))
        integral_x = sum(
            (x2 ** 2 + x2 * x1 + x1 ** 2) * (y2 - y1) for (x1, y1), (x2, y2) in zip(dots, dots[1:] + [dots[0]]))
        integral_y = -sum(
            (y2 ** 2 + y2 * y1 + y1 ** 2) * (x2 - x1) for (x1, y1), (x2, y2) in zip(dots, dots[1:] + [dots[0]]))
        answer = (3 * s * integral_x_sq + 3 * s * integral_y_sq - 2 * integral_x ** 2 - 2 * integral_y ** 2) / (
                9 * s ** 2)
        answers.append(f"{answer}")
    print(*answers, sep="\n")