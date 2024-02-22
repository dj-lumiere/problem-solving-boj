from itertools import product
from collections import Counter

s1, s2, s3 = map(int, input().split())
freq = Counter(map(sum, product(range(1, s1 + 1), range(1, s2 + 1), range(1, s3 + 1))))
max_freq = max(freq.values())
print(min(k for k, v in freq.items() if v == max_freq))