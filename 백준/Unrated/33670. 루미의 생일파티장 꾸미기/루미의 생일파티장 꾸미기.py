MOD = 998_244_353
n, l = map(int, input().split())
phi = [i for i in range(n + 1)]

phi_l = l
prime_factors = []
for i in range(2, int(l ** .5) + 1):
    if l % i == 0:
        prime_factors.append(i)
        while l % i == 0:
            l //= i
if l != 1:
    prime_factors.append(l)

for prime_factor in prime_factors:
    phi_l *= (prime_factor - 1)
    phi_l //= prime_factor

for i in range(2, n + 1):
    if phi[i] == i:
        for j in range(i, n + 1, i):
            phi[j] *= i - 1
            phi[j] //= i

for i in range(2, n + 1):
    for j in prime_factors:
        if i % j == 0:
            phi[i] //= (j - 1)
            phi[i] *= j

answer = sum(phi) * phi_l % MOD
print(answer)