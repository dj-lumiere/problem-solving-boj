# 8658 Liczba


def min_nondivisor(target):
    for i in range(1, 2 * int(target**0.5) + 1):
        if target % i:
            return i
    return int(target**0.5) + 1


n = int(input())
print(min_nondivisor(n), n - 1)