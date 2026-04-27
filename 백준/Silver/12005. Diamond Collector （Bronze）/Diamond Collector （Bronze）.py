import os
from collections import Counter
from itertools import permutations

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
        k = int(input())
        a = [int(input()) for _ in range(n)]
        a_count = Counter(a)
        max_displays = [0 for _ in range(10001)]
        for i in range(1, 10001):
            if i not in a_count:
                continue
            for j, v in a_count.items():
                if i > j or i + k < j:
                    continue
                max_displays[i] += v
        answer = f"{max(max_displays)}"
        answers[h] = answer
    print(answers)