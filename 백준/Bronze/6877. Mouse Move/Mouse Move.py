from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
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
        c = int(input())
        r = int(input())
        x, y = 0, 0
        while True:
            a = int(input())
            b = int(input())
            if a == 0 and b == 0:
                break
            new_x = x + a
            new_y = y + b
            new_x = max(0, min(c, new_x))
            new_y = max(0, min(r, new_y))
            x, y = new_x, new_y
            answer = f"{x} {y}"
            answers.append(f"{answer}")
    print(*answers, sep="\n")