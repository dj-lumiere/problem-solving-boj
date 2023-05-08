# 7964 Fibonacci Sums
from itertools import zip_longest
from sys import stdin

N1, *A1 = list(map(int, stdin.readline().strip().split(" ")))
N2, *A2 = list(map(int, stdin.readline().strip().split(" ")))

if A1 == [0] and A2 == [0]:
    print(1, 0)
else:
    N = max(N1, N2) + 3
    result = [i + j for (i, j) in zip_longest(A1, A2, fillvalue=0)]
    result.append(0)
    result.append(0)
    result.append(0)
    
    # First stage: Move from right to left, removing 2's
    for i in range(len(result) - 3, -1, -1):
        x = result[i]
        if result[i + 1 : i + 4] == [0, 2, 0]:
            result[i : i + 4] = [x + 1, 0, 0, 1]
        elif result[i + 1 : i + 4] == [0, 3, 0]:
            result[i : i + 4] = [x + 1, 0, 1, 1]
        elif result[i + 1 : i + 4] == [1, 2, 0]:
            result[i : i + 4] = [x, 0, 1, 1]
        elif result[i + 1 : i + 4] == [2, 1, 0]:
            result[i : i + 4] = [x, 1, 0, 1]
        if i == 0:
            # 2
            if result[i : i + 3] == [2, 0, 0]:
                result[i : i + 3] = [0, 1, 0]
            # 3
            elif result[i : i + 3] == [3, 0, 0]:
                result[i : i + 3] = [0, 0, 1]
            # 4
            elif result[i : i + 3] == [0, 2, 0]:
                result[i : i + 3] = [1, 0, 1]
            elif result[i : i + 3] == [2, 1, 0]:
                result[i : i + 3] = [1, 0, 1]
            # 5
            elif result[i : i + 3] == [2, 0, 1]:
                result[i : i + 3] = [0, 1, 1]
            elif result[i : i + 3] == [3, 1, 0]:
                result[i : i + 3] = [0, 1, 1]
            elif result[i : i + 3] == [1, 2, 0]:
                result[i : i + 3] = [0, 1, 1]
            # 6
            elif result[i : i + 3] == [0, 3, 0]:
                result[i : i + 3] = [1, 1, 1]
            elif result[i : i + 3] == [3, 0, 1]:
                result[i : i + 3] = [1, 1, 1]
            elif result[i : i + 3] == [2, 2, 0]:
                result[i : i + 3] = [1, 1, 1]
            elif result[i : i + 3] == [0, 0, 2]:
                result[i : i + 3] = [1, 1, 1]
    
    # Second stage: Move from left to right, removing consecutive 1's
    for i in range(len(result) - 2):
        if result[i : i + 3] == [1, 1, 0]:
            result[i : i + 3] = [0, 0, 1]
    
    # Third stage: Move from right to left, removing consecutive 1's
    for i in range(len(result) - 3, -1, -1):
        if result[i : i + 3] == [1, 1, 0]:
            result[i : i + 3] = [0, 0, 1]
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    print(len(result), *result)