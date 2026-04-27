import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n, m, k = [int(input()) for _ in range(3)]
        a = [[int(input()) for _ in range(m)] for _ in range(n)]
        accsum = [[0 for _ in range(m + 1)] for _ in range(n)]
        for j, v1 in enumerate(a):
            for l, v2 in enumerate(v1):
                accsum[j][l + 1] = v2 + accsum[j][l]
        result = [0 for _ in range(n)]
        for j, v1 in enumerate(accsum):
            for l, v2 in enumerate(v1):
                if v2 >= k:
                    result[j] = l
                    break
            else:
                result[j] = m + 1
        min_result = min(result)
        answer = result.index(min_result) + 1
        answers[i] = f"{answer} {min_result}"
    print(answers)