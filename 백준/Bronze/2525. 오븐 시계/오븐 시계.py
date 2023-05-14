# 2525 오븐 시계

A, B = list(map(int, input().split(" ")))
C = int(input())

B += C
A += B // 60
B %= 60
A %= 24

print(f"{A} {B}")