import os
from bisect import bisect_right, bisect_left

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        throws = [int(input()) for _ in range(n)]
        throws.sort()
        answer = 0
        for i in range(n):
            for j in range(n):
                if i >= j:
                    continue
                x = throws[i]
                y = throws[j]
                z_min = bisect_left(throws, y + (y - x))
                z_max = bisect_right(throws, y + 2 * (y - x))
                answer += z_max - z_min
        answers[h] = f"{answer}"
    print(answers)