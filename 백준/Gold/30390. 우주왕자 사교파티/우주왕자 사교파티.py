# 30390 우주왕자 사교파티
# GCD(A, B)가 답


A, B, K = map(int, input().split(" "))
divisors = []
for i in range(1, int((A + B) ** 0.5) + 1):
    if (A + B) % i == 0:
        divisors.extend([i, (A + B) // i])
possible_values = []
divisors = sorted(set(divisors))
for i in divisors:
    if (A % i + B % i == i or A % i == B % i == 0) and min(A % i, B % i) <= K:
        possible_values.append(i)
print(max(possible_values))