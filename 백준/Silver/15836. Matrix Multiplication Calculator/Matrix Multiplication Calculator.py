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
    t = INF
    answers = []
    for hh in range(t):
        M, N, P, Q = map(int, [input(), input(), input(), input()])
        A = [[int(input()) for _ in range(N)] for _ in range(M)]
        B = [[int(input()) for _ in range(Q)] for _ in range(P)]
        if M == 0 and N == 0 and P == 0 and Q == 0:
            break
        if N != P:
            answer = f"Case #{hh + 1}:\nundefined"
        else:
            C = [[0 for _ in range(Q)] for _ in range(M)]
            for i in range(M):
                for j in range(Q):
                    for k in range(N):
                        C[i][j] += A[i][k] * B[k][j]
            result = '\n'.join(["| " + ' '.join(map(str, row)) + " |" for row in C])
            answer = f"Case #{hh + 1}:\n{result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")