# 1086 박성원
from math import factorial, gcd
from sys import stdin


def input():
    return stdin.readline().strip()


N = int(input())
total_cases = factorial(N)
numbers = [input() for _ in range(N)]
number_length = [len(i) for i in numbers]
K = int(input())
numbers = [int(i) % K for i in numbers]
mod_power_of_10 = [1]
for _ in range(50):
    mod_power_of_10.append(mod_power_of_10[-1] * 10 % K)
dp = [[0 for _ in range(1 << N)] for _ in range(K)]
dp[0][0] = 1
for mask in range(1 << N):
    for remainder in range(K):
        if dp[remainder][mask] == 0:
            continue
        for i in range(N):
            if not (mask & (1 << i)):
                next_remainder = (
                    remainder * mod_power_of_10[number_length[i]] + numbers[i]
                ) % K
                dp[next_remainder][mask | (1 << i)] += dp[remainder][mask]
numerator = dp[0][(1 << N) - 1]
denominator = total_cases
divisor_for_reduction = gcd(numerator, denominator)
numerator, denominator = (
    numerator // divisor_for_reduction,
    denominator // divisor_for_reduction,
)
print(f"{numerator}/{denominator}")