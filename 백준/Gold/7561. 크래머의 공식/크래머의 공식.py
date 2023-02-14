# 7561 크래머의 공식
from decimal import Decimal

T = int(input())


def det_A(M: list[list[int]]) -> int:
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def det_A1(M: list[list[int]]) -> int:
    return (
        M[0][3] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][3] * M[2][2] - M[1][2] * M[2][3])
        + M[0][2] * (M[1][3] * M[2][1] - M[1][1] * M[2][3])
    )


def det_A2(M: list[list[int]]) -> int:
    return (
        M[0][0] * (M[1][3] * M[2][2] - M[1][2] * M[2][3])
        - M[0][3] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][3] - M[1][3] * M[2][0])
    )


def det_A3(M: list[list[int]]) -> int:
    return (
        M[0][0] * (M[1][1] * M[2][3] - M[1][3] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][3] - M[1][3] * M[2][0])
        + M[0][3] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


for i in range(1, T + 1):
    M = [list(map(int, input().split(" "))) for _ in range(3)]
    A = det_A(M)
    A1 = det_A1(M)
    A2 = det_A2(M)
    A3 = det_A3(M)
    print(A1, A2, A3, A, sep=" ")

    if A == 0:
        print("No unique solution")
    else:
        if abs(A1) * 2000 < abs(A):
            x1 = 0
        else:
            x1 = round(Decimal(A1) / Decimal(A), 3)
        if abs(A2) * 2000 < abs(A):
            x2 = 0
        else:
            x2 = round(Decimal(A2) / Decimal(A), 3)
        if abs(A3) * 2000 < abs(A):
            x3 = 0
        else:
            x3 = round(Decimal(A3) / Decimal(A), 3)
        print(f"Unique solution: {x1:0>.3f} {x2:0>.3f} {x3:0>.3f}")
    if i != T:
        print()