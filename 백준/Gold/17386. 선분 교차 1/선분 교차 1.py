# 17386 선분 교차 1

from fractions import Fraction

x1, y1, x2, y2 = list(map(int, input().split(" ")))
x3, y3, x4, y4 = list(map(int, input().split(" ")))

matrix = [[y1 - y2, x2 - x1], [y3 - y4, x4 - x3]]
det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
intercept = [y1 * (x2 - x1) - x1 * (y2 - y1), y3 * (x4 - x3) - x3 * (y4 - y3)]
if det:
    matrix_inv = [
        [Fraction(x4 - x3, det), Fraction(x1 - x2, det)],
        [Fraction(y4 - y3, det), Fraction(y1 - y2, det)],
    ]
    solution = [Fraction(0), Fraction(0)]
    for i in range(2):
        for j in range(2):
            solution[i] += matrix_inv[i][j] * intercept[j]
    if (
        min(x1, x2) <= solution[0] <= max(x1, x2)
        and min(x3, x4) <= solution[0] <= max(x3, x4)
        and min(y1, y2) <= solution[1] <= max(y1, y2)
        and min(y3, y4) <= solution[1] <= max(y3, y4)
    ):
        print(1)
    else:
        print(0)
else:
    print(0)