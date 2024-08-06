from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answers = []
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    for hh in range(t):
        a, b = map(int, input().split())
        answer = a + b
        answers.append(f"{answer}")
    print(*answers, sep="\n")
