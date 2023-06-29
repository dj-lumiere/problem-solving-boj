# 1712 손익분기점
from math import ceil

# A+BN<CN
A, B, C = map(int, input().split(" "))
break_even_point = A // (C - B) if B != C else -1
print(break_even_point + 1 if break_even_point >= 0 else -1)