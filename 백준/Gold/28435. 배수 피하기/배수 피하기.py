# 28435 배수 피하기
from math import ceil

# 나머지 간에는 독립적으로 배열이 구성 가능
# 나머지가 0 or 짝수인 K에 대해서 K//2인 경우에 대해서는 따로 생각
# 나머지 짝이 이어질 경우 2**smc[i]+2**smc[K-i]-1
# 1개거나 0개인 원소 제외
MOD = 1_000_000_007
N, K = map(int, input().split(" "))
same_mod_count = [0] * K
A = list(map(int, input().split(" ")))
for v in A:
    same_mod_count[v % K] += 1
result = 1
for i in range(1, ceil(K / 2)):
    result_sub = pow(2, same_mod_count[i], MOD) + pow(2, same_mod_count[K - i], MOD) - 1
    result = result * result_sub % MOD
result = result * (same_mod_count[0] + 1) % MOD
if not K & 1:
    result = result * (same_mod_count[K // 2] + 1) % MOD
result -= N + 1
result %= MOD
print(result)