# 21864 이산로그가 장난이냐?

a_2000000 = 108600338365753046
mod = 10**18 + 31
N = int(input())
result = a_2000000
for _ in range(2000000, N, -1):
    result = pow(42, result, mod)
print(result)