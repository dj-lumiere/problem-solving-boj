import os
from collections import Counter
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        x = int(input())
        answer = x - 1
        for n in range(60, 2, -1):
            start = 1
            end = int(x ** (1 / (n-1))) * 2
            while start + 1 < end:
                mid = (start + end) // 2
                if mid ** n - x * mid + x - 1 > 0:
                    end = mid
                elif mid ** n - x * mid + x - 1 < 0:
                    start = mid
                else:
                    answer = min(mid, answer)
                    found_answer = True
                    break
        answers[h] = f"Case #{h + 1}: {answer}"
    print(answers)