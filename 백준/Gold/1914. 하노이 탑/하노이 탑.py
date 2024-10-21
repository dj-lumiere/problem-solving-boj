from sys import setrecursionlimit, stdout, stderr

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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        K = 2 ** N - 1
        moves = []
        answers.append(K)
        if N <= 20:
            stack = [(N, 1, 2, 3)]
            while stack:
                n, src, aux, dst = stack.pop()
                if n == 1:
                    moves.append(f"{src} {dst}")
                    continue
                stack.extend([(n - 1, aux, src, dst), (1, src, aux, dst), (n - 1, src, dst, aux)])
            answers.extend(moves)
    print(*answers, sep="\n")
