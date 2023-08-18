# 2087 암호문

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
        sums_dict[total_value] = status


def find_configuration(numbers, target) -> str:
    n = len(numbers)
    n1, n2 = n // 2, n - n // 2
    sums_left = {}
    sums_right = {}
    for status in range(1, 1 << n1):
        register_combination(sums_left, status, n1, numbers, 0)
    for status in range(1, 1 << n2):
        register_combination(sums_right, status, n2, numbers, n1)
    configuration = ""
    for value, status in sums_left.items():
        if target - value in sums_right:
            configuration += ("0" * (n1 - len(bin(status)[2:])) + bin(status)[2:])[::-1]
            configuration += (
                "0" * (n2 - len(bin(sums_right[target - value])[2:]))
                + bin(sums_right[target - value])[2:]
            )[::-1]
            return configuration


N = int(input())
numbers = [int(input()) for _ in range(N)]
target = int(input())
print(find_configuration(numbers, target))