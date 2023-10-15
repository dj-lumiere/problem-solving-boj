# 14860 GCD 곱

from sys import stdin, stdout

input = stdin.readline
print = stdout.write


# a까지의 소수를 찾기
def find_prime(a: int) -> list[int]:
    if a == 1:
        return []
    finder_limit = a
    prime_list: list[bool] = [True for i in range(0, finder_limit + 1)]
    prime_list[0] = False
    prime_list[1] = False
    for x in range(1, int(finder_limit**0.5) + 1):
        if prime_list[x]:
            prime_list[x : finder_limit + 1 : x] = [False] * (finder_limit // x)
            prime_list[x] = True
    return [i for i, v in enumerate(prime_list) if v]


N, M = map(int, input().split(" "))
grid_size = max(N, M)
prime_list = find_prime(grid_size)
power_list = [0 for _ in range(len(prime_list))]
answer = 1
MOD = 10**9 + 7
for index, value in enumerate(prime_list):
    next_value = value
    while next_value <= grid_size:
        power_list[index] += (N // next_value) * (M // next_value)
        next_value *= value
for prime, power in zip(prime_list, power_list):
    answer *= pow(prime, power, MOD)
    answer %= MOD
print(f"{answer}")