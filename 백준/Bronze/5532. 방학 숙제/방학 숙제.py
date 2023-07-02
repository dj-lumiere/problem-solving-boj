# 5532 방학 숙제
from math import ceil

L, A, B, C, D = int(input()), int(input()), int(input()), int(input()), int(input())
print(L - max(ceil(B / D), ceil(A / C)))