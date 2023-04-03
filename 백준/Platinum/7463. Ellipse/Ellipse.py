# 7463 Ellipse

from fractions import Fraction
from decimal import Decimal

pi = Decimal("3.141592653589793238462643383279")


def quintic_matrix_determinant(matrix: list[list[int]]) -> int:
    return (
        (matrix[2][2] * matrix[1][1] * matrix[0][0])
        * (matrix[3][3] * matrix[4][4] - matrix[4][3] * matrix[3][4])
        + (-(matrix[3][2] * matrix[1][1] * matrix[0][0]))
        * (matrix[2][3] * matrix[4][4] - matrix[4][3] * matrix[2][4])
        + (matrix[4][2] * matrix[1][1] * matrix[0][0])
        * (matrix[2][3] * matrix[3][4] - matrix[3][3] * matrix[2][4])
        + (-(matrix[1][2] * matrix[2][1] * matrix[0][0]))
        * (matrix[3][3] * matrix[4][4] - matrix[4][3] * matrix[3][4])
        + (matrix[3][2] * matrix[2][1] * matrix[0][0])
        * (matrix[1][3] * matrix[4][4] - matrix[4][3] * matrix[1][4])
        + (-(matrix[4][2] * matrix[2][1] * matrix[0][0]))
        * (matrix[1][3] * matrix[3][4] - matrix[3][3] * matrix[1][4])
        + (matrix[1][2] * matrix[3][1] * matrix[0][0])
        * (matrix[2][3] * matrix[4][4] - matrix[4][3] * matrix[2][4])
        + (-(matrix[2][2] * matrix[3][1] * matrix[0][0]))
        * (matrix[1][3] * matrix[4][4] - matrix[4][3] * matrix[1][4])
        + (matrix[4][2] * matrix[3][1] * matrix[0][0])
        * (matrix[1][3] * matrix[2][4] - matrix[2][3] * matrix[1][4])
        + (-(matrix[1][2] * matrix[4][1] * matrix[0][0]))
        * (matrix[2][3] * matrix[3][4] - matrix[3][3] * matrix[2][4])
        + (matrix[2][2] * matrix[4][1] * matrix[0][0])
        * (matrix[1][3] * matrix[3][4] - matrix[3][3] * matrix[1][4])
        + (-(matrix[3][2] * matrix[4][1] * matrix[0][0]))
        * (matrix[1][3] * matrix[2][4] - matrix[2][3] * matrix[1][4])
        + (-(matrix[2][2] * matrix[0][1] * matrix[1][0]))
        * (matrix[3][3] * matrix[4][4] - matrix[4][3] * matrix[3][4])
        + (matrix[3][2] * matrix[0][1] * matrix[1][0])
        * (matrix[2][3] * matrix[4][4] - matrix[4][3] * matrix[2][4])
        + (-(matrix[4][2] * matrix[0][1] * matrix[1][0]))
        * (matrix[2][3] * matrix[3][4] - matrix[3][3] * matrix[2][4])
        + (matrix[0][2] * matrix[2][1] * matrix[1][0])
        * (matrix[3][3] * matrix[4][4] - matrix[4][3] * matrix[3][4])
        + (-(matrix[3][2] * matrix[2][1] * matrix[1][0]))
        * (matrix[0][3] * matrix[4][4] - matrix[4][3] * matrix[0][4])
        + (matrix[4][2] * matrix[2][1] * matrix[1][0])
        * (matrix[0][3] * matrix[3][4] - matrix[3][3] * matrix[0][4])
        + (-(matrix[0][2] * matrix[3][1] * matrix[1][0]))
        * (matrix[2][3] * matrix[4][4] - matrix[4][3] * matrix[2][4])
        + (matrix[2][2] * matrix[3][1] * matrix[1][0])
        * (matrix[0][3] * matrix[4][4] - matrix[4][3] * matrix[0][4])
        + (-(matrix[4][2] * matrix[3][1] * matrix[1][0]))
        * (matrix[0][3] * matrix[2][4] - matrix[2][3] * matrix[0][4])
        + (matrix[0][2] * matrix[4][1] * matrix[1][0])
        * (matrix[2][3] * matrix[3][4] - matrix[3][3] * matrix[2][4])
        + (-(matrix[2][2] * matrix[4][1] * matrix[1][0]))
        * (matrix[0][3] * matrix[3][4] - matrix[3][3] * matrix[0][4])
        + (matrix[3][2] * matrix[4][1] * matrix[1][0])
        * (matrix[0][3] * matrix[2][4] - matrix[2][3] * matrix[0][4])
        + (matrix[1][2] * matrix[0][1] * matrix[2][0])
        * (matrix[3][3] * matrix[4][4] - matrix[4][3] * matrix[3][4])
        + (-(matrix[3][2] * matrix[0][1] * matrix[2][0]))
        * (matrix[1][3] * matrix[4][4] - matrix[4][3] * matrix[1][4])
        + (matrix[4][2] * matrix[0][1] * matrix[2][0])
        * (matrix[1][3] * matrix[3][4] - matrix[3][3] * matrix[1][4])
        + (-(matrix[0][2] * matrix[1][1] * matrix[2][0]))
        * (matrix[3][3] * matrix[4][4] - matrix[4][3] * matrix[3][4])
        + (matrix[3][2] * matrix[1][1] * matrix[2][0])
        * (matrix[0][3] * matrix[4][4] - matrix[4][3] * matrix[0][4])
        + (-(matrix[4][2] * matrix[1][1] * matrix[2][0]))
        * (matrix[0][3] * matrix[3][4] - matrix[3][3] * matrix[0][4])
        + (matrix[0][2] * matrix[3][1] * matrix[2][0])
        * (matrix[1][3] * matrix[4][4] - matrix[4][3] * matrix[1][4])
        + (-(matrix[1][2] * matrix[3][1] * matrix[2][0]))
        * (matrix[0][3] * matrix[4][4] - matrix[4][3] * matrix[0][4])
        + (matrix[4][2] * matrix[3][1] * matrix[2][0])
        * (matrix[0][3] * matrix[1][4] - matrix[1][3] * matrix[0][4])
        + (-(matrix[0][2] * matrix[4][1] * matrix[2][0]))
        * (matrix[1][3] * matrix[3][4] - matrix[3][3] * matrix[1][4])
        + (matrix[1][2] * matrix[4][1] * matrix[2][0])
        * (matrix[0][3] * matrix[3][4] - matrix[3][3] * matrix[0][4])
        + (-(matrix[3][2] * matrix[4][1] * matrix[2][0]))
        * (matrix[0][3] * matrix[1][4] - matrix[1][3] * matrix[0][4])
        + (-(matrix[1][2] * matrix[0][1] * matrix[3][0]))
        * (matrix[2][3] * matrix[4][4] - matrix[4][3] * matrix[2][4])
        + (matrix[2][2] * matrix[0][1] * matrix[3][0])
        * (matrix[1][3] * matrix[4][4] - matrix[4][3] * matrix[1][4])
        + (-(matrix[4][2] * matrix[0][1] * matrix[3][0]))
        * (matrix[1][3] * matrix[2][4] - matrix[2][3] * matrix[1][4])
        + (matrix[0][2] * matrix[1][1] * matrix[3][0])
        * (matrix[2][3] * matrix[4][4] - matrix[4][3] * matrix[2][4])
        + (-(matrix[2][2] * matrix[1][1] * matrix[3][0]))
        * (matrix[0][3] * matrix[4][4] - matrix[4][3] * matrix[0][4])
        + (matrix[4][2] * matrix[1][1] * matrix[3][0])
        * (matrix[0][3] * matrix[2][4] - matrix[2][3] * matrix[0][4])
        + (-(matrix[0][2] * matrix[2][1] * matrix[3][0]))
        * (matrix[1][3] * matrix[4][4] - matrix[4][3] * matrix[1][4])
        + (matrix[1][2] * matrix[2][1] * matrix[3][0])
        * (matrix[0][3] * matrix[4][4] - matrix[4][3] * matrix[0][4])
        + (-(matrix[4][2] * matrix[2][1] * matrix[3][0]))
        * (matrix[0][3] * matrix[1][4] - matrix[1][3] * matrix[0][4])
        + (matrix[0][2] * matrix[4][1] * matrix[3][0])
        * (matrix[1][3] * matrix[2][4] - matrix[2][3] * matrix[1][4])
        + (-(matrix[1][2] * matrix[4][1] * matrix[3][0]))
        * (matrix[0][3] * matrix[2][4] - matrix[2][3] * matrix[0][4])
        + (matrix[2][2] * matrix[4][1] * matrix[3][0])
        * (matrix[0][3] * matrix[1][4] - matrix[1][3] * matrix[0][4])
        + (matrix[1][2] * matrix[0][1] * matrix[4][0])
        * (matrix[2][3] * matrix[3][4] - matrix[3][3] * matrix[2][4])
        + (-(matrix[2][2] * matrix[0][1] * matrix[4][0]))
        * (matrix[1][3] * matrix[3][4] - matrix[3][3] * matrix[1][4])
        + (matrix[3][2] * matrix[0][1] * matrix[4][0])
        * (matrix[1][3] * matrix[2][4] - matrix[2][3] * matrix[1][4])
        + (-(matrix[0][2] * matrix[1][1] * matrix[4][0]))
        * (matrix[2][3] * matrix[3][4] - matrix[3][3] * matrix[2][4])
        + (matrix[2][2] * matrix[1][1] * matrix[4][0])
        * (matrix[0][3] * matrix[3][4] - matrix[3][3] * matrix[0][4])
        + (-(matrix[3][2] * matrix[1][1] * matrix[4][0]))
        * (matrix[0][3] * matrix[2][4] - matrix[2][3] * matrix[0][4])
        + (matrix[0][2] * matrix[2][1] * matrix[4][0])
        * (matrix[1][3] * matrix[3][4] - matrix[3][3] * matrix[1][4])
        + (-(matrix[1][2] * matrix[2][1] * matrix[4][0]))
        * (matrix[0][3] * matrix[3][4] - matrix[3][3] * matrix[0][4])
        + (matrix[3][2] * matrix[2][1] * matrix[4][0])
        * (matrix[0][3] * matrix[1][4] - matrix[1][3] * matrix[0][4])
        + (-(matrix[0][2] * matrix[3][1] * matrix[4][0]))
        * (matrix[1][3] * matrix[2][4] - matrix[2][3] * matrix[1][4])
        + (matrix[1][2] * matrix[3][1] * matrix[4][0])
        * (matrix[0][3] * matrix[2][4] - matrix[2][3] * matrix[0][4])
        + (-(matrix[2][2] * matrix[3][1] * matrix[4][0]))
        * (matrix[0][3] * matrix[1][4] - matrix[1][3] * matrix[0][4])
    )


def gaussian_elimination(matrix: list[list[int]], size: int) -> list[Fraction]:
    new_matrix: list[list[Fraction]] = [
        [Fraction(matrix[i][j]) for j in range(size + 1)] for i in range(size)
    ]

    for h in range(0, size):
        # Swap rows if necessary
        if new_matrix[h][h] == 0:
            for k in range(h + 1, size):
                if new_matrix[k][h] != 0:
                    new_matrix[h], new_matrix[k] = new_matrix[k], new_matrix[h]
                    break

        for i in range(h + 1, size):
            if new_matrix[h][h] != 0:
                multiplier = new_matrix[i][h] / new_matrix[h][h]
                for j in range(h, size + 1):
                    new_matrix[i][j] -= new_matrix[h][j] * multiplier

    for i in range(size - 1, 0 - 1, -1):
        if new_matrix[i][i] != 0:
            multiplier = new_matrix[i][size] / new_matrix[i][i]
            new_matrix[i][i] = Fraction(1)
            new_matrix[i][size] = multiplier
            for j in range(i - 1, 0 - 1, -1):
                new_matrix[j][size] -= new_matrix[j][i] * multiplier
                new_matrix[j][i] = Fraction(0, 1)

    solution: list[Fraction] = [new_matrix[i][size] for i in range(size)]
    return solution


def dots_to_equation_matrix(values: list[int]) -> list[list[int]]:
    matrix: list[list[int]] = [
        [
            values[2 * i] ** 2,
            values[2 * i] * values[2 * i + 1],
            values[2 * i + 1] ** 2,
            values[2 * i],
            values[2 * i + 1],
            1,
        ]
        for i in range(5)
    ]
    return matrix


def is_solvable(matrix: list[list[int]]) -> bool:
    det = quintic_matrix_determinant(matrix)
    return bool(det)


def get_area(ellipse_equation: list[Fraction]) -> str:
    # 타원을 Ax^2+2Hxy+By^2+2Gx+2Fy+C=0 형태로 나타내기
    A, H, B, G, F, C = ellipse_equation
    H, G, F = H / 2, G / 2, F / 2
    # A가 음수일 경우 A를 양수로 만들어주기
    if A < 0:
        A, H, B, G, F, C = -A, -H, -B, -G, -F, -C
    # 타원/원 여부를 결정하는 판별식
    is_ellipse: Fraction = A * B - H**2
    # 실타원 여부를 결정하는 판별식
    is_real: Fraction = A * F**2 + B * G**2 + C * H**2 - A * B * C - 2 * F * G * H
    # B^2-4AC < 0 and L > 0인지 확인 (실타원 여부 결정)
    if is_ellipse > 0 and is_real > 0:
        is_ellipse_decimal: Decimal = Decimal(is_ellipse.numerator) / Decimal(
            is_ellipse.denominator
        )
        is_real_decimal: Decimal = Decimal(is_real.numerator) / Decimal(
            is_real.denominator
        )
        # S = pi*is_real/(is_ellipse^2)^1.5
        result: Decimal = (
            pi * is_real_decimal / (is_ellipse_decimal * is_ellipse_decimal.sqrt())
        )
        answer = f"{result:.6f}"
    else:
        answer = "IMPOSSIBLE"
    return answer


k = int(input())
for _ in range(k):
    values = [int(i) for i in input().split(" ") if i]
    for i in range(5):
        values = [i + 1001 for i in values]
    # 일단 Ax^2+Bxy+Cy^2+Dx+Ey=1 형태로 만들기
    matrix = dots_to_equation_matrix(values)
    # 일단 x^2+Bxy+Cy^2+Dx+Ey+F=0 형태로 만들기
    matrix2 = [matrix[a][1:] + [-matrix[a][0]] for a in range(5)]
    is_solvable_check: bool = True
    shift_one_block: bool = False
    ellipse_equation: list[Fraction] = []
    # 1번이 풀이 가능하면 그냥 품
    if is_solvable(matrix):
        shift_one_block = False
    # 1번이 풀이 불가능하면 상수항이 0일 수 있으니
    elif is_solvable(matrix2):
        shift_one_block = True
    else:
        is_solvable_check = False
    if is_solvable_check and shift_one_block:
        # 상수항 대신 x^2 계수를 1로 고정함
        ellipse_equation = [Fraction(1)] + gaussian_elimination(matrix2, 5)
        print(get_area(ellipse_equation))
    elif is_solvable_check and not shift_one_block:
        # 타원을 형성하기 위한 5원1차 연립방정식을 우변이 1이 되게 풀었으므로, 이항하면 C = -1
        ellipse_equation = gaussian_elimination(matrix, 5) + [Fraction(-1)]
        print(get_area(ellipse_equation))
    else:
        print("IMPOSSIBLE")