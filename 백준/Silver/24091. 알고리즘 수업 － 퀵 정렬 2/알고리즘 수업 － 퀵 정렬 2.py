import os
import re
from collections import Counter
from sys import setrecursionlimit
setrecursionlimit(100000)

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    keumminsoo = [i for i in range(1000001) if all(j == "4" or j == "7" for j in str(i))]
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        k = int(input())
        a = [int(input()) for _ in range(n)]
        change_count = 0


        def partition(A, p, r):
            global change_count
            x = A[r]
            y = p
            for j in range(p, r):
                if A[j] <= x:
                    if change_count < k:
                        A[y], A[j] = A[j], A[y]
                        y += 1
                        change_count += 1
            if y != r:
                if change_count < k:
                    A[y], A[r] = A[r], A[y]
                    change_count += 1
            return y


        def quick_sort(A, p, r):
            if p >= r:
                return
            q = partition(A, p, r)
            quick_sort(A, p, q - 1)
            quick_sort(A, q + 1, r)


        quick_sort(a, 0, len(a) - 1)

        if change_count < k:
            answers[i] = "-1"
        else:
            answers[i] = " ".join(map(str, a))
    print(answers)