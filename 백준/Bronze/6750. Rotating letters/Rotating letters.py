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
        word = list(input().decode())
        answers[i] = f'{"YES" if all(i in ["I", "O", "S", "H", "Z", "X", "N"] for i in word) else "NO"}'
    # while True:
    #     n = int(input())
    #     if n == 0:
    #         break
    #     a = [int(input()) for _ in range(n)]
    #     answers.append("\n".join(map(str, reversed(a)))+"\n0")
    print(answers)