import os
from itertools import product

tokens = iter(os.read(0, os.fstat(0).st_size).split())
N = int(next(tokens))
A = [int(next(tokens)) for _ in range(N)]
B = [int(next(tokens)) for _ in range(N)]
a_sum = sum(A)
b_sum = sum(B)
min_pair = {a: 0 for a in range(1, 1000000 + 1)}
min_values = {a: 0 for a in range(1, 1000000 + 1)}
for a in min_pair:
    b_candidate = a * a_sum // b_sum
    min_values_sub = [abs(a * a_sum - b * b_sum) for b in range(b_candidate - 1, b_candidate + 2)]
    b = min_values_sub.index(min(min_values_sub)) + b_candidate - 1
    min_pair[a] = b
    min_values[a] = min(min_values_sub)
min_value = min(min_values.values())
for a in min_values:
    if min_values[a] == min_value:
        print(a, min_pair[a])
        break