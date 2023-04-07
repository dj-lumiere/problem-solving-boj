# 27875 파이파이 (1)

from math import floor

def bbp_formula(n: int):
    pi = 0
    coefficients = (16, -16, -8, -16, -4, -4, 2)
    k = 0
    # 정수부들을 합함
    for k in range(n + 1):
        pi_k = sum(
            [
                j * pow(16, n - k, (8 * k + i + 1) ** 2) / (8 * k + i + 1) ** 2
                for (i, j) in enumerate(coefficients)
            ]
        )
        pi += pi_k
    # 소수부들을 합함
    k = n + 1
    while True:
        pi_k = sum(
            [
                j * 16 ** (n - k) / (8 * k + i + 1) ** 2
                for (i, j) in enumerate(coefficients)
            ]
        )
        pi += pi_k
        if abs(pi_k) < 0.00001:
            break
        k += 1
    return pi


def get_nth_hex_digit_of_pi(n: int):
    pi = bbp_formula(n - 1)
    nth_digit = int((pi - floor(pi)) * 16)
    return format(nth_digit, "X")


n = int(input())
print(get_nth_hex_digit_of_pi(n))