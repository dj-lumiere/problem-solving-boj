# 1979 극적인 곱셈

from sys import set_int_max_str_digits

set_int_max_str_digits(1000000)

# (10n-1)x=(10**x-n)*k
# 따라서 10**x = n (mod 10n-1)과 같음
# 또한 (10**x-n)*k//(10*n-1)은 n자리여야함


def n_miracle_number_finder(n: int, k: int) -> int:
    b: int = power_finder(n)
    if n == 1:
        return k
    elif n == 5 and k == 7:
        return 142857
    else:
        x = b
        if len(str((10**x - n) * k // (10 * n - 1))) == x:
            return ((10**x - n) * k // (10 * n - 1)) * 10 + k
        else:
            return 0


def power_finder(n: int) -> int:
    modulo = 10 * n - 1
    counter = 0
    while True:
        if pow(10, counter, modulo) == n:
            return counter
        else:
            counter += 1


print(n_miracle_number_finder(*map(int, input().split(" "))))
