# 15873 공백 없는 A+B
from itertools import product

result = {}
for i, j in product(range(1, 11), repeat=2):
    result[str(i) + str(j)] = i + j
ab = input()
print(result[ab])