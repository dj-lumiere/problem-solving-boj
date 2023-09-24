# 11025 요세푸스 문제 3

N, K = map(int, input().split(" "))

result = [0] * N
for i in range(N):
    if i == 0:
        result[i] = 1
        continue
    result[i] = (result[i - 1] + K - 1) % (i + 1) + 1
print(result[-1])