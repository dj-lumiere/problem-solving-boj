# 3177 크로아티아 수열
from math import log10, floor


one_digit_initial = "AJDTXPXSOD"  # (1~9)
teen_digit_initial = "DJDTXPXSOD"  # (10~19)
two_digit_initial = "AADTXPXSOD"  # (20~90)
three_digit_initial = "ASDTXPXSOD"  # (100~900)
four_digit_initial = "ATDTXPXSOD"  # (1000~9000)
seven_digit_initial = "AMDTXPXSOD"  # (1000~9000)


def digit_length(target: int) -> int:
    if target == 0:
        return 1
    return floor(log10(target))


def find_nth_digit(target: int, n: int) -> int:
    return target // (10**n) % 10


def count_initials_at_ith_digit(
    upper_limit: int, digit_order: int, digit_initials: str
) -> tuple[dict[str, int], int]:
    result = {"D": 0, "J": 0, "M": 0, "O": 0, "P": 0, "S": 0, "T": 0, "X": 0, "A": 0}
    removed_number = 0
    for i in range(10):
        nth_digit = (
            find_nth_digit(upper_limit, digit_order)
            if upper_limit < 10 ** (digit_order + 1)
            else 10
        )
        if nth_digit < i:
            removable_number = 0
        elif nth_digit == i:
            removable_number = upper_limit % (10**digit_order) + 1
        else:
            removable_number = 10**digit_order
        if digit_initials[i] == "A":
            continue
        result[digit_initials[i]] += removable_number
        removed_number += removable_number
    return result, removed_number


def count_initials_special(
    upper_limit: int, digit_order: int, digit_initials: str
) -> tuple[dict[str, int], int]:
    result = {"D": 0, "J": 0, "M": 0, "O": 0, "P": 0, "S": 0, "T": 0, "X": 0, "A": 0}
    removed_number = 0
    for i in range(10):
        nth_digit = (
            find_nth_digit(upper_limit, digit_order)
            if upper_limit < 20 * 10**digit_order
            else 10
        )
        if nth_digit < i:
            removable_number = 0
        elif nth_digit == i:
            removable_number = upper_limit % (10**digit_order) + 1
        else:
            removable_number = 10**digit_order
        result[digit_initials[i]] += removable_number
        removed_number += removable_number
    return result, removed_number


def count_initials(upper_limit: int, target_initial: str) -> int:
    result = {"D": 0, "J": 0, "M": 0, "O": 0, "P": 0, "S": 0, "T": 0, "X": 0, "A": 0}
    leftover_numbers = upper_limit
    for digit_order in range(digit_length(upper_limit) + 1):
        if digit_order == 0:
            subresult, removed_number = count_initials_at_ith_digit(
                upper_limit, digit_order, one_digit_initial
            )
            for key, value in subresult.items():
                result[key] += value
            leftover_numbers -= removed_number
        elif digit_order == 3:
            subresult, removed_number = count_initials_at_ith_digit(
                upper_limit, digit_order, four_digit_initial
            )
            for key, value in subresult.items():
                result[key] += value
            leftover_numbers -= removed_number
        elif digit_order > 3 and digit_order % 3 == 0:
            subresult, removed_number = count_initials_at_ith_digit(
                upper_limit, digit_order, seven_digit_initial
            )
            for key, value in subresult.items():
                result[key] += value
            leftover_numbers -= removed_number
        elif digit_order % 3 == 1:
            subresult1, removed_number = count_initials_special(
                upper_limit, digit_order - 1, teen_digit_initial
            )
            leftover_numbers -= removed_number
            subresult, removed_number = count_initials_at_ith_digit(
                upper_limit, digit_order, two_digit_initial
            )
            for key, value in subresult1.items():
                result[key] += value
            for key, value in subresult.items():
                result[key] += value
            leftover_numbers -= removed_number
        elif digit_order % 3 == 2:
            subresult, removed_number = count_initials_at_ith_digit(
                upper_limit, digit_order, three_digit_initial
            )
            for key, value in subresult.items():
                result[key] += value
            leftover_numbers -= removed_number
    return result[target_initial]


def find_nth_initial(initial: str, n: int) -> int:
    bisect_start = 1
    bisect_end = 10**13
    while bisect_start + 1 < bisect_end:
        bisect_mid = (bisect_start + bisect_end) // 2
        result = count_initials(bisect_mid, initial)
        if result >= n:
            bisect_end = bisect_mid
        else:
            bisect_start = bisect_mid
    return bisect_end


initial, n_str = input().split(" ")
result = find_nth_initial(initial, int(n_str))
print(result)