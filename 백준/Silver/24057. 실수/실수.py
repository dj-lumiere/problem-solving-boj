# 24171 복소수

from math import gcd, lcm
from fractions import Fraction

A_value_list: list[int] = list(map(int, input().split(" ")))
B_value_list: list[int] = list(map(int, input().split(" ")))
# A의 실수부의 유리수부
Arr: Fraction = Fraction(A_value_list[1], A_value_list[0])
# A의 실수부의 무리수부
Ari: Fraction = Fraction(A_value_list[2], A_value_list[0])
# B의 실수부의 유리수부
Brr: Fraction = Fraction(B_value_list[1], B_value_list[0])
# B의 실수부의 무리수부
Bri: Fraction = Fraction(B_value_list[2], B_value_list[0])
# 루트 안의 숫자 (모두 동일)
d: int = A_value_list[3]
# a0 b0 c0 d

# 덧셈, 뺄셈
# 각각의 유리수부와 무리수부를 더하거나 빼기
add_fraction_list: list[Fraction] = [Arr + Brr, Ari + Bri]
sub_fraction_list: list[Fraction] = [Arr - Brr, Ari - Bri]


# 곱셈
# 무리수부와 무리수부를 곱하면 d배가 되고, 
multiply_fraction_list: list[Fraction] = [
    Arr * Brr + Ari * Bri * d,
    Ari * Brr + Arr * Bri,
]


# 나눗셈
# B**-1 구하기 위해 분자의 실수화, 이후 유리화 진행
# 분자의 실수화 및 유리화 진행 후 남은 계수
p: Fraction = Brr**2 - Bri**2 * d
# B**-1 = (Brr-Bri*sqrt(d))/(p**2-q**2*d)
B_inv: list[Fraction] = [
    Brr,
    -Bri,
]
B_inv = [i / p for i in B_inv]
Crr, Cri = B_inv
division_fraction_list: list[Fraction] = [
    Arr * Crr + Ari * Cri * d,
    Ari * Crr + Arr * Cri,
]


def fraction_list_to_list(fraction_list: list[Fraction]) -> list[int]:
    # 실수부 분모 통분
    a0 = lcm(fraction_list[0].denominator, fraction_list[1].denominator)
    # 실수부의 유리수부
    b0 = fraction_list[0].numerator * (a0 // fraction_list[0].denominator)
    # 실수부의 무리수부
    c0 = fraction_list[1].numerator * (a0 // fraction_list[1].denominator)
    # c0가 0이면 d0도 0이 나와야함
    d0 = d if c0 != 0 else 0
    return [a0, b0, c0, d0]


add_list = fraction_list_to_list(add_fraction_list)
sub_list = fraction_list_to_list(sub_fraction_list)
multiply_list = fraction_list_to_list(multiply_fraction_list)
division_list = fraction_list_to_list(division_fraction_list)

print(*add_list, sep=" ")
print(*sub_list, sep=" ")
print(*multiply_list, sep=" ")
print(*division_list, sep=" ")