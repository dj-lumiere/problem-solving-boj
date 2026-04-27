import os
from bisect import bisect_left

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        c = [int(input()) for _ in range(n)]
        c.sort()
        max_fee = 0
        price = 0
        for j in range(1, c[-1] + 1):
            cow_count = n - bisect_left(c, j)
            fee = cow_count * j
            if fee > max_fee:
                max_fee = fee
                price = j
        answers[i] = f"{max_fee} {price}"
    print(answers)