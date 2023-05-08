# 14854 이항 계수 6

from itertools import zip_longest
from sys import stdin, stdout


def n_ary_change(x, n) -> list[int]:
    next_x = x
    change_list = []
    while next_x:
        change_list.append(next_x % n)
        next_x //= n
    return change_list


nCr_list = [
    [[0 for r in range(11 + 1)] for n in range(11 + 1)],
    [[0 for r in range(13 + 1)] for n in range(13 + 1)],
    [[0 for r in range(37 + 1)] for n in range(37 + 1)],
]

C_list = [11, 13, 37, 27]
for i in range(3):
    for n in range(C_list[i] + 1):
        for r in range(C_list[i] + 1):
            if n < r:
                nCr_list[i][n][r] = 0
            elif n == 0:
                nCr_list[i][n][r] = 1
            elif n == r or r == 0:
                nCr_list[i][n][r] = 1
            else:
                nCr_list[i][n][r] = (
                    nCr_list[i][n - 1][r - 1] + nCr_list[i][n - 1][r]
                ) % C_list[i]

coprime_with_3_accumulated_product = [1]
for i in range(1, 27 + 1):
    if not i % 3:
        coprime_with_3_accumulated_product.append(
            coprime_with_3_accumulated_product[-1]
        )
    else:
        coprime_with_3_accumulated_product.append(
            coprime_with_3_accumulated_product[-1] * i % 27
        )


def power_3_count_in_x_factorial(x: int) -> int:
    answer = 0
    answer_sub = 1
    next_factor = 3
    while answer_sub:
        answer_sub = x // next_factor
        next_factor *= 3
        answer += answer_sub
    return answer


def x_factorial_with_coprime_with_3_modulo_27(x: int) -> int:
    answer = 1
    next_factor = 1
    while next_factor <= x:
        batches, leftover = divmod(x // next_factor, 27)
        answer *= pow(coprime_with_3_accumulated_product[27], batches, 27)
        answer *= coprime_with_3_accumulated_product[leftover]
        answer %= 27
        next_factor *= 3
    return answer


s_list = (
    pow(13 * 27 * 37, -1, 11),
    pow(11 * 27 * 37, -1, 13),
    pow(11 * 13 * 27, -1, 37),
    pow(11 * 13 * 37, -1, 27),
)

n_list = (13 * 27 * 37, 11 * 27 * 37, 11 * 13 * 27, 11 * 13 * 37)

T = int(stdin.readline().strip())
for _ in range(T):
    A, B = (int(i) for i in stdin.readline().strip().split(" "))
    # 뤼카 정리 활용
    mod_list = []
    for i, C in enumerate(C_list):
        if i != 3:
            a_list = n_ary_change(A, C)
            b_list = n_ary_change(B, C)
            answer = 1
            for n, r in zip_longest(a_list, b_list, fillvalue=0):
                answer = answer * nCr_list[i][n][r] % C
            mod_list.append(answer)
    # 27로 나눈 나머지를 구하기...
    n_factorial_mod_27_with_coprime_to_3 = x_factorial_with_coprime_with_3_modulo_27(A)
    r_factorial_mod_27_with_coprime_to_3 = x_factorial_with_coprime_with_3_modulo_27(B)
    n_minus_r_factorial_mod_27_with_coprime_to_3 = (
        x_factorial_with_coprime_with_3_modulo_27(A - B)
    )
    power_3_count = (
        power_3_count_in_x_factorial(A)
        - power_3_count_in_x_factorial(A - B)
        - power_3_count_in_x_factorial(B)
    )
    if power_3_count >= 3:
        power_3_de_facto_count = 3
    else:
        power_3_de_facto_count = power_3_count % 3
    nCr_mod_27 = (
        (n_factorial_mod_27_with_coprime_to_3)
        * (
            pow(n_minus_r_factorial_mod_27_with_coprime_to_3, -1, 27)
            * pow(r_factorial_mod_27_with_coprime_to_3, -1, 27)
        )
        * pow(3, power_3_de_facto_count)
    ) % 27
    # CRT 파트
    mod_list.append(nCr_mod_27)
    answer = (
        sum([a_i * n_i * s_i for a_i, n_i, s_i in zip(mod_list, n_list, s_list)])
        % 142857
    )
    stdout.writelines(str(answer) + "\n")
