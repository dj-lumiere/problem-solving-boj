from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


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
        M, N, K, W = (int(input()) for _ in range(4))
        A = [[int(input()) for _ in range(N)] for _ in range(M)]
        B = [[0 for _ in range(N - W + 1)] for _ in range(M - W + 1)]
        for i in range(M - W + 1):
            for j in range(N - W + 1):
                window = []
                for x in range(W):
                    for y in range(W):
                        window.append(A[i + x][j + y])
                window.sort()
                B[i][j] = window[len(window) // 2]
        answer = '\n'.join(' '.join(map(str, row)) for row in B)
        answers.append(f"{answer}")
    print(*answers, sep="\n")