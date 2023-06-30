# 14215 세 막대

side1, side2, side3 = map(int, input().split(" "))
side1, side2, side3 = sorted([side1, side2, side3])
side3 = min(side3, side1 + side2 - 1)
print(side1 + side2 + side3)