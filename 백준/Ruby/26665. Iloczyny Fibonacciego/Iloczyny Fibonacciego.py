# 26665 Iloczyny Fibonacciego
from sys import stdin, stdout

def ntt(a: list[int], invert: bool, root: int, mod: int):
    n = len(a)
    a = bit_reversal_permutation(a)
    size = 2
    root_of_unity = [0] * (n // 2)
    if invert:
        angle = mod - 1 - (mod - 1) // n
    else:
        angle = (mod - 1) // n
    root_of_unity[0] = 1
    angleth_power = pow(root, angle, mod)
    for i in range(1, n // 2):
        root_of_unity[i] = root_of_unity[i - 1] * angleth_power % mod

    while size <= n:
        step = n // size
        for i in range(0, n, size):
            w = 1
            for j in range(size // 2):
                omega = root_of_unity[step * j]
                u = a[i + j]
                v = a[i + j + size // 2] * omega % mod
                a[i + j] = (u + v) % mod
                a[i + j + size // 2] = (u - v) % mod
        size <<= 1
    if invert:
        ntt_coefficient_normalization(a, mod)
    return a


def bit_reversal_permutation(a: list[int]) -> list[int]:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while not ((j := j ^ bit) & bit):
            bit >>= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    return a


def ntt_coefficient_normalization(a, mod):
    n = len(a)
    n_inv = pow(n, -1, mod)
    for i in range(n):
        a[i] = a[i] * n_inv % mod


def multiply_ntt(a, b, root, mod):
    transformed_a = a[:]
    transformed_b = b[:]
    n = 1
    while n < len(a) + len(b):
        n <<= 1
    transformed_a += [0] * (n - len(transformed_a))
    transformed_b += [0] * (n - len(transformed_b))
    ntt(transformed_a, False, root, mod)
    ntt(transformed_b, False, root, mod)
    for i in range(n):
        transformed_a[i] = transformed_a[i] * transformed_b[i] % mod
    ntt(transformed_a, True, root, mod)
    for index, value in enumerate(transformed_a):
        if value > mod // 2:
            transformed_a[index] -= mod
    return transformed_a[: len(a) + len(b)]


def zeckendorf_to_lucas(target):
    if len(target) < 3:
        target += [0] * (3 - len(target))
    result = [0] * (len(target) + 1)
    for index in range(len(target) - 1, 2, -1):
        if target[index - 2 : index + 1] == [0, 0, 1]:
            target[index - 2 : index + 1] = [1, 1, 0]
        elif target[index - 2 : index + 1] == [1, 0, 1]:
            target[index - 2 : index + 1] = [0, 0, 0]
            result[index + 1] += 1
        elif index >= 3 and target[index - 3 : index + 1] == [0, 0, 1, 1]:
            target[index - 3 : index + 1] = [1, 0, 0, 0]
            result[index + 1] += 1
        elif index >= 3 and target[index - 3 : index + 1] == [1, 0, 1, 1]:
            target[index - 3 : index + 1] = [0, 1, 1, 0]
            result[index] += 1
        elif index >= 3 and target[index - 3 : index + 1] == [0, 1, 1, 1]:
            target[index - 3 : index + 1] = [0, 0, 1, 0]
            result[index + 1] += 1
    last_value = target[0] * 1 + target[1] * 2 + target[2] * 3
    if last_value == 1:
        result[1] += 1
    elif last_value == 2:
        result[0] += 1
    elif last_value == 3:
        result[2] += 1
    elif last_value == 4:
        result[3] += 1
    elif last_value == 5:
        result[1] += 1
        result[3] += 1
    elif last_value == 6:
        result[0] += 1
        result[3] += 1
    return result


def coefficient_normalization_for_add_and_sub(
    subtraction_check: bool, result: list[int]
) -> list[int]:
    if subtraction_check:
        coefficient_normalization_sub_pass(result)
    coefficient_normalization_pass1(result)
    coefficient_normalization_pass2(result)
    coefficient_normalization_pass3(result)
    return result


def coefficient_normalization_sub_pass(result):
    for index in range(len(result) - 2, -1, -1):
        if result[index : index + 3] == [0, 0, 1]:
            result[index : index + 3] = [1, 1, 0]
        elif result[index : index + 3] == [0, 0, 2]:
            result[index : index + 3] = [1, 1, 1]
        elif result[index : index + 3] == [0, -1, 1]:
            result[index : index + 3] = [1, 0, 0]
        elif result[index : index + 3] == [0, -1, 2]:
            result[index : index + 3] = [1, 0, 1]
        elif result[index : index + 3] == [1, -1, 1]:
            result[index : index + 3] = [2, 0, 0]
        elif result[index : index + 3] == [1, -1, 2]:
            result[index : index + 3] = [2, 0, 1]
        elif result[index : index + 3] == [-1, 0, 1]:
            result[index : index + 3] = [0, 1, 0]
        elif result[index : index + 3] == [-1, 0, 2]:
            result[index : index + 3] = [0, 1, 1]


def coefficient_normalization_pass1(result):
    for index in range(len(result) - 3, -1, -1):
        if result[index + 1 : index + 4] == [0, 2, 0]:
            result[index] += 1
            result[index + 1 : index + 4] = [0, 0, 1]
        elif result[index + 1 : index + 4] == [0, 3, 0]:
            result[index] += 1
            result[index + 1 : index + 4] = [0, 1, 1]
        elif result[index + 1 : index + 4] == [1, 2, 0]:
            result[index + 1 : index + 4] = [0, 1, 1]
        elif result[index + 1 : index + 4] == [2, 1, 0]:
            result[index + 1 : index + 4] = [1, 0, 1]
    s = result[0] * 1 + result[1] * 2 + result[2] * 3
    if s == 0:
        result[:3] = [0, 0, 0]
    elif s == 1:
        result[:3] = [1, 0, 0]
    elif s == 2:
        result[:3] = [0, 1, 0]
    elif s == 3:
        result[:3] = [0, 0, 1]
    elif s == 4:
        result[:3] = [1, 0, 1]
    elif s == 5:
        result[:3] = [0, 1, 1]
    elif s == 6:
        result[:3] = [1, 1, 1]


def coefficient_normalization_pass2(result):
    for index in range(len(result) - 2):
        if result[index : index + 3] == [1, 1, 0]:
            result[index : index + 3] = [0, 0, 1]


def coefficient_normalization_pass3(result):
    for index in range(len(result) - 3, -1, -1):
        if result[index : index + 3] == [1, 1, 0]:
            result[index : index + 3] = [0, 0, 1]


def phinary_to_lucas(target):
    index_zero_point = (len(target) - 1) // 2
    digits_in_lucas = len(target) - index_zero_point
    result = [0] * digits_in_lucas
    result[0] = target[index_zero_point] // 2
    for index in range(1, len(result)):
        result[index] = target[index + index_zero_point]
    return result


def lucas_to_zeckendorf(target):
    # L(N) = F(N+1) + F(N-1) = Z(N-1)+Z(N-3)
    result = [0] * (len(target) - 1)
    for index in range(1, len(target)):
        result[index - 1] += target[index]
    for index in range(3, len(target)):
        result[index - 3] += target[index]
    result[0] += target[0] * 2 + target[2]
    return result


def zeckendorf_addition(target1, target2):
    result = [0] * len(target1)
    for index in range(len(target1)):
        result[index] += target1[index]
    for index in range(len(target2)):
        result[index] += target2[index]
    result = coefficient_normalization_for_add_and_sub(False, result)
    return result


def zeckendorf_subtraction(target1, target2):
    result = [0] * len(target1)
    for index in range(len(target1)):
        result[index] += target1[index]
    for index in range(len(target2)):
        result[index] -= target2[index]
    result = coefficient_normalization_for_add_and_sub(True, result)
    return result


def remove_trailing_zero(target):
    while target and target[-1] == 0:
        target.pop()


def lucas_to_phinary(target):
    result = [0] * (len(target) * 2 - 1)
    result[len(target) - 1] = target[0] * 2
    for index in range(1, len(target)):
        result[len(target) + index - 1] += target[index]
        result[len(target) - index - 1] += -target[index]
        if index % 2 == 0:
            result[len(target) - index - 1] += target[index] * 2
    return result


def coefficient_normalization(target):
    target = target + [0] * len(target)
    negative_coefficient = [0] * (len(target) + 3)
    positive_coefficient = [0] * (len(target) + 3)
    for index in range(len(target)):
        if target[index] > 0:
            positive_coefficient[index] = target[index]
        elif target[index] < 0:
            negative_coefficient[index] = -target[index]
    for index in range(len(positive_coefficient) - 1):
        if positive_coefficient[index] > 0 and positive_coefficient[index + 1] > 0:
            delta = min(positive_coefficient[index], positive_coefficient[index + 1])
            positive_coefficient[index] -= delta
            positive_coefficient[index + 1] -= delta
            positive_coefficient[index + 2] += delta
        if negative_coefficient[index] > 0 and negative_coefficient[index + 1] > 0:
            delta = min(negative_coefficient[index], negative_coefficient[index + 1])
            negative_coefficient[index] -= delta
            negative_coefficient[index + 1] -= delta
            negative_coefficient[index + 2] += delta
    positive_result = [0] * (len(target) + 3)
    negative_result = [0] * (len(target) + 3)
    positive_indexth_bit = [0] * (len(target) + 3)
    negative_indexth_bit = [0] * (len(target) + 3)
    result = []
    positive_bit_size = max(positive_coefficient).bit_length()
    negative_bit_size = max(negative_coefficient).bit_length()
    bit_size = max(positive_bit_size, negative_bit_size) + 1
    for index in range(bit_size, -1, -1):
        for index2 in range(len(positive_coefficient)):
            positive_indexth_bit[index2] = (
                positive_coefficient[index2] & (1 << index)
            ) >> index
            negative_indexth_bit[index2] = (
                negative_coefficient[index2] & (1 << index)
            ) >> index
        positive_result = zeckendorf_addition(positive_result, positive_result)
        negative_result = zeckendorf_addition(negative_result, negative_result)
        positive_result = zeckendorf_addition(positive_result, positive_indexth_bit)
        negative_result = zeckendorf_addition(negative_result, negative_indexth_bit)
    result = zeckendorf_subtraction(positive_result, negative_result)
    return result


def main():
    input = stdin.readline
    print = stdout.write
    test_cases = int(input().strip())
    for _ in range(test_cases):
        _, *target1 = list(map(int, input().strip().split()))
        _, *target2 = list(map(int, input().strip().split()))
        target1 = zeckendorf_to_lucas(target1)
        target2 = zeckendorf_to_lucas(target2)
        target1 = lucas_to_phinary(target1)
        target2 = lucas_to_phinary(target2)
        result = multiply_ntt(target1, target2, 3, 998244353)
        result_sub = phinary_to_lucas(result)
        result_sub2 = lucas_to_zeckendorf(result_sub)
        result_sub3 = coefficient_normalization(result_sub2)
        remove_trailing_zero(result_sub3)
        if len(result_sub3) == 0:
            result_sub3.append(0)
        result_sub3_string = " ".join(map(str, result_sub3))
        print(f"{len(result_sub3)} {result_sub3_string}\n")


main()