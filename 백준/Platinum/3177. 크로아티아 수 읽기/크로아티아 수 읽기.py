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


def find_nth_digit(target: int, n: int, is_teen: bool) -> int:
    threshold = (2 if is_teen else 1) * 10 ** (n + 1)
    if target >= threshold:
        return 10
    return target // (10**n) % 10


def count_removable_number(
    upper_limit: int, digit_order: int, i: int, is_teen: bool
) -> int:
    nth_digit = find_nth_digit(upper_limit, digit_order, is_teen)
    if nth_digit < i:
        return 0
    elif nth_digit == i:
        return upper_limit % (10**digit_order) + 1
    else:
        return 10**digit_order


def count_initials_at_ith_digit(upper_limit: int, digit_order: int) -> dict[str, int]:
    result = {"D": 0, "J": 0, "M": 0, "O": 0, "P": 0, "S": 0, "T": 0, "X": 0, "A": 0}
    digit_initials = select_digit_string(digit_order)
    if digit_order % 3 == 1:
        subresult = count_initials_teens(upper_limit, digit_order - 1)
        for key, value in subresult.items():
            result[key] += value
    for i in range(10):
        removable_number = count_removable_number(upper_limit, digit_order, i, False)
        result[digit_initials[i]] += removable_number
    return result


def count_initials_teens(upper_limit: int, digit_order: int) -> dict[str, int]:
    result = {"D": 0, "J": 0, "M": 0, "O": 0, "P": 0, "S": 0, "T": 0, "X": 0, "A": 0}
    for i in range(10):
        removable_number = count_removable_number(upper_limit, digit_order, i, True)
        result[teen_digit_initial[i]] += removable_number
    return result


def select_digit_string(digit_order: int) -> str:
    if digit_order == 0:
        return one_digit_initial
    if digit_order == 3:
        return four_digit_initial
    if digit_order % 3 == 0:
        return seven_digit_initial
    if digit_order % 3 == 1:
        return two_digit_initial
    if digit_order % 3 == 2:
        return three_digit_initial
    return ""


def count_initials(upper_limit: int, target_initial: str) -> int:
    result = {"D": 0, "J": 0, "M": 0, "O": 0, "P": 0, "S": 0, "T": 0, "X": 0, "A": 0}
    for digit_order in range(digit_length(upper_limit) + 1):
        subresult = count_initials_at_ith_digit(upper_limit, digit_order)
        for key, value in subresult.items():
            result[key] += value
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
