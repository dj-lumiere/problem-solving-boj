# 1208 부분수열의 합 2

from sys import stdin


def input():
    return stdin.readline().strip()


def register_combination(sums_dict, status, size, numbers, offset):
    total_value = 0
    for i in range(size):
        if not (status >> i) & 1:
            continue
        total_value += numbers[offset + i]
    if total_value not in sums_dict:
        sums_dict[total_value] = 1
    else:
        sums_dict[total_value] += 1


def find_configuration(numbers, target) -> int:
    n = len(numbers)
    if n == 1:
        return int(numbers[0] == target)
    n1, n2 = n // 2, n - n // 2
    sums_left = {0: 1}
    sums_right = {0: 1}
    for status in range(1, 1 << n1):
        register_combination(sums_left, status, n1, numbers, 0)
    for status in range(1, 1 << n2):
        register_combination(sums_right, status, n2, numbers, n1)
    # print(sums_left, sums_right)
    result = 0
    for value, count in sums_left.items():
        if target - value in sums_right:
            result += count * sums_right[target - value]
    return result - (0 if target else 1)


N, S = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))
print(find_configuration(numbers, S))