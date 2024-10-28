from math import factorial
from functools import reduce
N, M = map(int, input().split())
if N>=M:
    print(0)
else:
    print(reduce(lambda x,y:x*y%M, range(1, N+1), 1))