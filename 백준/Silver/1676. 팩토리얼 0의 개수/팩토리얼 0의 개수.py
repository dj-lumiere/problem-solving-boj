from math import log

x = int(input())

def factorial_zeroes(N: int) -> int:

    if not N:
        return 0

    else:
        count_2 = 0
        count_5 = 0

        maximum_power_2 = int(log(N, 2))
        maximum_power_5 = int(log(N, 5))

        for i in range(1, maximum_power_2 + 1):
            count_2 += (N // (2 ** i))

        for i in range(1, maximum_power_5 + 1):
            count_5 += (N // (5 ** i))

        return min(count_2, count_5)

print(factorial_zeroes(x))