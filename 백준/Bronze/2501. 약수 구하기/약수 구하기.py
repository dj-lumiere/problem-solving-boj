# 2501 약수 구하기

divisor_count = 1
N, K = map(int, input().split(" "))
divisor = [0] * (N + 1)
for i in range(1, N + 1):
    if not N % i:
        divisor[divisor_count] = i
        divisor_count += 1
print(divisor[K])