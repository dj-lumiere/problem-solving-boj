# 2985 세 수

from itertools import product

a, b, c = map(int, input().split())
for i1, i2 in product(["==", "+", "-", "*", "//"], repeat=2):
    if i1 != "==" and i2 != "==":
        continue
    if i1 == "==" and i2 == "==":
        continue
    if eval(f"{a}{i1}{b}{i2}{c}"):
        print(f"{a}{i1}{b}{i2}{c}".replace("==", "=").replace("//", "/"))
        break