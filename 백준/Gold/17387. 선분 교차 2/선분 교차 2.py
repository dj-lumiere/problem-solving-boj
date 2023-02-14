# 20149 선분 교차 3

from fractions import Fraction
from decimal import Decimal

x1, y1, x2, y2 = list(map(int, input().split(" ")))
x3, y3, x4, y4 = list(map(int, input().split(" ")))

matrix = [[y1 - y2, x2 - x1], [y3 - y4, x4 - x3]]
det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
intercept = [y1 * (x2 - x1) - x1 * (y2 - y1), y3 * (x4 - x3) - x3 * (y4 - y3)]
if det:
    matrix_inv = [
        [Fraction(matrix[1][1], det), Fraction(-1 * matrix[0][1], det)],
        [Fraction(-1 * matrix[1][0], det), Fraction(matrix[0][0], det)],
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
    ratio_list = []
    invalid_ratio = False
    if matrix[1][0] != 0:
        ratio_list.append(Fraction(matrix[0][0], matrix[1][0]))
    elif matrix[1][0] == 0 and matrix[0][0] != 0:
        invalid_ratio = True
    if matrix[1][1] != 0:
        ratio_list.append(Fraction(matrix[0][1], matrix[1][1]))
    elif matrix[1][1] == 0 and matrix[0][1] != 0:
        invalid_ratio = True
    if intercept[1] != 0:
        ratio_list.append(Fraction(intercept[0], intercept[1]))
    elif intercept[1] == 0 and intercept[0] != 0:
        invalid_ratio = True
    # 평행할 때
    if len(set(ratio_list)) != 1 or invalid_ratio:
        print(0)
    # 평행하지 않을 때
    else:
        range_x1 = [min(x1, x2), max(x1, x2)]
        range_x2 = [min(x3, x4), max(x3, x4)]
        if range_x1[0] > range_x2[0]:
            range_x1, range_x2 = range_x2, range_x1
        range_y1 = [min(y1, y2), max(y1, y2)]
        range_y2 = [min(y3, y4), max(y3, y4)]
        if range_y1[0] > range_y2[0]:
            range_y1, range_y2 = range_y2, range_y1
        # 한 점에서 만남
        if range_x1[1] == range_x2[0] and range_y1[1] == range_y2[0]:
            print(1)
        # 범위가 겹침
        elif (
            range_x1[0] <= range_x2[0] <= range_x1[1]
            and range_x1[0] <= range_x2[1] <= range_x1[1]
            and range_y1[0] <= range_y2[0] <= range_y1[1]
            and range_y1[0] <= range_y2[1] <= range_y1[1]
        ) or (
            range_x1[0] <= range_x2[0] <= range_x1[1]
            and range_x2[0] <= range_x1[1] <= range_x2[1]
            and range_y1[0] <= range_y2[0] <= range_y1[1]
            and range_y2[0] <= range_y1[1] <= range_y2[1]
        ):
            print(1)
        # 범위가 안 겹침
        else:
            print(0)