from sys import stderr, stdout


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, "")
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        b = [int(input()) for _ in range(n)]
        answer = sum(3 if a[i] > b[i] else 1 if a[i] == b[i] else 0 for i in range(n))
        answers.append(f"{answer}")
    print(*answers, sep="\n")