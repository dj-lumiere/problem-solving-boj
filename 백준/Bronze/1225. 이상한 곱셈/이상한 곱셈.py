# 1225 이상한 곱셈

from itertools import product

A, B = map(list, input().split(" "))
A_digits = list(map(int, A))
B_digits = list(map(int, B))
print(sum(a_digit * b_digit for a_digit, b_digit in product(A_digits, B_digits)))