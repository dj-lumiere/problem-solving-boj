# 10386 Con + (tin / (ued + (Frac / tions)))

from fractions import Fraction
from math import floor


def fraction_to_continued_fractions(target_fraction: Fraction) -> list[int]:
    target_fraction_list: list[int] = []
    if target_fraction != 0:
        target_fraction_list_0th = floor(target_fraction)
        target_fraction -= floor(target_fraction)
        while True:
            if target_fraction.denominator == 1:
                target_fraction_list.append(int(target_fraction))
                break
            else:
                target_fraction_list.append(int(target_fraction))
                target_fraction -= int(target_fraction)
                target_fraction = 1 / target_fraction
        target_fraction_list[0] = target_fraction_list_0th
    else:
        target_fraction_list.append(0)
    return target_fraction_list


def continued_fraction_list_to_fraction(continued_fraction: list[int]) -> Fraction:
    continued_fraction = continued_fraction[::-1]
    result = Fraction(0)
    for (i, j) in enumerate(continued_fraction):
        if i == 0:
            result += j
        else:
            result = j + (1 / result)
    return result


case_number = 1
while True:
    N, M = list(map(int, input().split()))
    if not N and not M:
        break
    else:
        r1 = continued_fraction_list_to_fraction(list(map(int, input().split())))
        r2 = continued_fraction_list_to_fraction(list(map(int, input().split())))
        plus_list = fraction_to_continued_fractions(r1 + r2)
        minus_list = fraction_to_continued_fractions(r1 - r2)
        multiply_list = fraction_to_continued_fractions(r1 * r2)
        division_list = fraction_to_continued_fractions(r1 / r2)
        print(f"Case {case_number}:")
        print(*plus_list)
        print(*minus_list)
        print(*multiply_list)
        print(*division_list)
        case_number += 1
