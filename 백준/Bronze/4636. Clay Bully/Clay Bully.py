from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    answers = []
    for case_num in range(1, t + 1):
        n = int(input())
        if n == -1:
            break
        students = [(int(input()), int(input()), int(input()), input()) for _ in range(n)]
        volumes = [(s[3], s[0] * s[1] * s[2]) for s in students]
        bully = max(volumes, key=lambda x: x[1])
        victim = min(volumes, key=lambda x: x[1])
        answers.append(f"{bully[0]} took clay from {victim[0]}.")
    print(*answers, sep="\n")