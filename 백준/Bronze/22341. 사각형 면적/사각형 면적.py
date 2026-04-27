import os
from fractions import Fraction

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
        c = int(input())
        size = [n, n]
        for _ in range(c):
            x, y = int(input()), int(input())
            v_candidate = -1
            h_candidate = -1
            v_passed = False
            h_passed = False
            if x < size[0]:
                h_candidate = x * size[1]
            else:
                h_candidate = size[0] * size[1]
                h_passed = True
            if y < size[1]:
                v_candidate = y * size[0]
            else:
                v_candidate = size[0] * size[1]
                v_passed = True
            if v_candidate > h_candidate:
                size = [size[0], y] if not v_passed else [size[0], size[1]]
            else:
                size = [x, size[1]] if not h_passed else [size[0], size[1]]
        answer = size[0] * size[1]
        answers[h] = f"{answer}"
    print(answers)