# 13439 팩토리얼과 점화식
from sys import stdin, stdout
from itertools import product

input = stdin.readline
print = stdout.write
MOD = 1_000_000_009


# a까지의 소수를 찾기
def find_prime(a: int) -> list[int]:
    if a == 1:
        return []
    finder_limit = a
    prime_list: list[int] = [1 for i in range(0, finder_limit + 1)]
    prime_list[0] = 0
    prime_list[1] = 0
    for x in range(1, int(finder_limit**0.5) + 1):
        if not prime_list[x]:
            continue
        prime_list[x : finder_limit + 1 : x] = [0] * (finder_limit // x)
        prime_list[x] = 1
    return [i for i, v in enumerate(prime_list) if v]


prime_list = find_prime(1000)

# k -> n -> prime_factors
S = [[[0 for _ in range(len(prime_list))] for _ in range(1001)] for _ in range(101)]
for i, v in enumerate(prime_list):
    next_v = v
    while next_v <= 1000:
        for j in range(next_v, 1001, next_v):
            S[0][j][i] += 1
        next_v *= v

for k, n in product(range(101), range(1001)):
    if n == 0 or k == 0:
        continue
    S[k][n] = [i + j for i, j in zip(S[k][n - 1], S[k - 1][n])]

N, K = map(int, input().split(" "))
prime_factors = S[K][N]
result = 1
for v in prime_factors:
    result = result * (v + 1) % MOD
print(f"{result}")