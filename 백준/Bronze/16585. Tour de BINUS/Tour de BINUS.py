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
        a = [int(input()) for _ in range(n)]
        x1 = int(input())
        d1 = input()
        x2 = int(input())
        d2 = input()
        if d1 == "left":
            ayu_sum = sum(a[:x1])
        else:
            ayu_sum = sum(a[x1 - 1:])
        if d2 == "left":
            budi_count = a[:x2].count(0)
        else:
            budi_count = a[x2 - 1:].count(0)
        answer = f"{ayu_sum} {budi_count}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")