from math import log

x, y = list(map(int, input().split(" ")))

def factorial_twos(N: int) -> int:

    if not N:
        return 0

    else:
        count_2 :int = 0
        maximum_power_2 :int = int(log(N, 2))
        for i in range(1, maximum_power_2 + 1):
            count_2 += (N // (2 ** i))
        return count_2

def factorial_fives(N: int) -> int:

    if not N:
        return 0

    else:
        count_5 :int = 0
        maximum_power_5 :int = int(log(N, 5))
        for i in range(1, maximum_power_5 + 1):
            count_5 += (N // (5 ** i))
        return count_5

final_count_2 = factorial_twos(x)-(factorial_twos(y)+factorial_twos(x-y))
final_count_5 = factorial_fives(x)-(factorial_fives(y)+factorial_fives(x-y))

print(min(final_count_2, final_count_5))