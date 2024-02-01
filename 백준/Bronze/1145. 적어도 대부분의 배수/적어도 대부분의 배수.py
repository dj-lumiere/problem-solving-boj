# 1145 적어도 대부분의 배수

from itertools import combinations
from math import lcm

n = list(map(int, input().split()))
print(min(map(lambda a: lcm(*a), combinations(n, r=3))))