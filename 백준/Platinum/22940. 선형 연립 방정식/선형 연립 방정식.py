# 22940 선형 연립 방정식

from fractions import Fraction

N = int(input())
matrix = [list(map(Fraction, input().split(" "))) for _ in range(N)]

for h in range(0, N):
    for i in range(h + 1, N):
        for j in range(i, N):
            multiplier = Fraction(matrix[j][h]) / Fraction(matrix[h][h])
            for k in range(h, N + 1):
                matrix[j][k] -= matrix[h][k] * multiplier
for l in range(N-1, 0-1, -1):
    multiplier = Fraction(matrix[l][N]) / Fraction(matrix[l][l])
    matrix[l][l] = Fraction(1)
    matrix[l][N] = multiplier
    for m in range(l-1, 0-1, -1):
        matrix[m][N] -= matrix[m][l] * multiplier
        matrix[m][l] = Fraction(0,1)

solution = [int(matrix[i][N]) for i in range(N)]
print(" ".join(map(str, solution)))