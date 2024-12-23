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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        C = int(input())
        B = int(input())
        n = int(input())
        r = int(input())
        bailed = set()
        for _ in range(B):
            bailed.add(int(input()))
        total = 0
        for _ in range(n):
            ci = int(input())
            pi = int(input())
            if ci in bailed:
                total += pi * r // 100
        answers.append(f"Data Set {hh}:")
        answers.append(f"{total}")
        answers.append("")
    print(*answers, sep="\n")