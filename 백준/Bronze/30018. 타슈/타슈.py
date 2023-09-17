# 30018 타슈

N = int(input())
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
print(sum(abs(a - b) for a, b in zip(A, B)) // 2)