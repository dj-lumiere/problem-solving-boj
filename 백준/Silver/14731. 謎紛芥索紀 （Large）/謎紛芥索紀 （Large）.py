# 14731 謎紛芥索紀 (Large)

from sys import stdin

value = 0
N = int(input())

# 2의 승수를 10**9+7로 나눈 나머지 미리 계산해두기
# 10**9까지니 32개만 계산해두기
power_list = [2]
for i in range(31):
    power_list.append(power_list[-1] ** 2 % (10**9 + 7))


def binary_index(N):
    binary_list = [0 for i in range(32)]
    next_number = N
    for i in range(32):
        next_number, binary_list[i] = divmod(next_number, 2)
    return binary_list


# 미분계수를 구해서 더하기
for _ in range(N):
    c, k = list(map(int, stdin.readline().rstrip().split()))
    value_sub = c * k
    k_list = binary_index(k - 1)
    for i, j in zip(k_list, power_list):
        if i == 1:
            value_sub *= i * j
            value_sub %= 10**9 + 7
    value += value_sub
    value %= 10**9 + 7
print(value)
