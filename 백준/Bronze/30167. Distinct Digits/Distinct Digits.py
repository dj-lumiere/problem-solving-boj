# 30167 Distinct Digits

from itertools import product

l, r = map(int, input().split())
result = [False for _ in range(100001)]
for a in range(1, 5 + 1):
    for b in product(range(10), repeat=a):
        if any(sum(d == c for d in b) != 1 for c in b):
            continue
        result[int("".join(map(str, b)))] = True

for i in range(l, r + 1):
    if result[i]:
        print(i)
        break
else:
    print(-1)