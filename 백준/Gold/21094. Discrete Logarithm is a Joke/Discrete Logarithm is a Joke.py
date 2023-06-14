# 21094 Discrete Logarithm is a Joke

a_1000000 = 300
mod = 10**18 + 31
N = int(input())
result = a_1000000
for _ in range(1000000, N, -1):
    result = pow(42, result, mod)
print(result)