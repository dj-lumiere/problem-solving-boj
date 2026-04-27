# D번 - 사전 순 최대 공통 부분 수열

from bisect import bisect_left
from itertools import product, combinations
from sys import stdin
from typing import List

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    N = int(input())
    A = [int(input()) for _ in range(N)]
    M = int(input())
    B = [int(input()) for _ in range(M)]
    result = []
    a_index = []
    b_index = []
    for i in range(100, 0, -1):
        if not (i in A and i in B):
            continue
        if not result:
            result.append(i)
            a_index.append(A.index(i))
            b_index.append(B.index(i))
        while True:
            if i in A[a_index[-1] + 1:] and i in B[b_index[-1] + 1:]:
                result.append(i)
                a_index.append(A.index(i, a_index[-1] + 1))
                b_index.append(B.index(i, b_index[-1] + 1))
            else:
                break
    print(len(result))
    print(*result)
