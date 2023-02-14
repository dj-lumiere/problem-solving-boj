# 11021 A+B - 7
N = int(input())
for i in range(1, N + 1):
    print(f'Case #{i}: {sum(list(map(int, input().split(" "))))}')