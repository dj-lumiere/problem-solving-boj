from fractions import Fraction
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
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        matrix = [[Fraction(int(input())) for _ in range(N + 1)] for _ in range(N)]
        for h in range(N):
            if matrix[h][h] == 0:
                next_row_to_swap = h + 1
                for i in range(h + 1, N):
                    if matrix[i][h] != 0:
                        next_row_to_swap = i
                        break
                matrix[h], matrix[next_row_to_swap] = matrix[next_row_to_swap], matrix[h]
            for i in range(h + 1, N):
                for j in range(i, N):
                    eprint(h, i, j)
                    multiplier = Fraction(matrix[j][h]) / Fraction(matrix[h][h])
                    for k in range(h, N + 1):
                        matrix[j][k] -= matrix[h][k] * multiplier
        for l in reversed(range(N)):
            multiplier = Fraction(matrix[l][N]) / Fraction(matrix[l][l])
            matrix[l][l] = Fraction(1)
            matrix[l][N] = multiplier
            for m in range(l - 1, 0 - 1, -1):
                matrix[m][N] -= matrix[m][l] * multiplier
                matrix[m][l] = Fraction(0, 1)
        solution = [int(matrix[i][N]) for i in range(N)]
        answer = " ".join(map(str, solution))
        answers.append(f"{answer}")
    print(*answers, sep="\n")