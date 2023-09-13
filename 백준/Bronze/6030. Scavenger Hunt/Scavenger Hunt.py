# 6030 Scavenger Hunt
from itertools import product

P, Q = map(int, input().split(" "))
p_divisors = []
q_divisors = []

for i in range(1, int(P**0.5) + 1):
    if P % i:
        continue
    p_divisors.extend([i, P // i])

for i in range(1, int(Q**0.5) + 1):
    if Q % i:
        continue
    q_divisors.extend([i, Q // i])

p_divisors = list(set(p_divisors))
q_divisors = list(set(q_divisors))
p_divisors.sort()
q_divisors.sort()

for i, j in product(p_divisors, q_divisors):
    print(i, j)