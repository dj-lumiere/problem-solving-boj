import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 10001
    answers = ["" for _ in range(t)]
    for h in range(t):
        n1, n2 = int(input()), int(input())
        a = input().decode().strip()
        b = input().decode().strip()
        n = int(input())
        direction = [1 for _ in range(n1)] + [-1 for _ in range(n2)]
        ants = list(reversed(a)) + list(b)
        for _ in range(n):
            swap_pairs = []
            for i, v in enumerate(direction):
                if i == 0:
                    continue
                if v * -1 == direction[i - 1] and direction[i - 1] == 1:
                    swap_pairs.append((i - 1, i))
            for i, j in swap_pairs:
                ants[i], ants[j] = ants[j], ants[i]
                direction[i], direction[j] = direction[j], direction[i]
        answer = "".join(ants)
        answers[h] = f"{answer}"
    print(answers)