# B번 - 특별한 작은 분수

x, N = list(map(int, input().split(" ")))

for i in range(N):
    if not x % 2:
        x = (x >> 1) ^ 6
    else:
        x = (x << 1) ^ 6
print(x)