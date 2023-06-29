# 10817 세 수

A, B, C = map(int, input().split(" "))

if A < B:
    A, B = B, A
if B < C:
    B, C = C, A
if A < B:
    A, B = B, A
print(B)