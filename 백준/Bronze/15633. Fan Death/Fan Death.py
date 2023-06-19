# 15633 Fan Death
N = int(input())
divisors = []
for i in range(1, int(N**.5) + 1):
    if N % i == 0:
        divisors += [i, N // i] if i**2 != N else [i]
print(sum(divisors) * 5 - 24)