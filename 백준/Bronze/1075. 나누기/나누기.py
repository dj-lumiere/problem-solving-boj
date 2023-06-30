# 1075 나누기

N = int(input())
F = int(input())
result = 100
for i in range(100):
    if (N // 100 * 100 + i) % F == 0:
        result = min(result, i % 100)
print(f"{result:0>2}")