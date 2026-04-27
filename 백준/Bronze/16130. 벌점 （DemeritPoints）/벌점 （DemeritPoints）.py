import os
from functools import reduce
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = [int(j, base=36) for j in input().decode()]
        answer = 0
        current_value = 0
        is_weapon = False
        is_09 = False
        for j, v in enumerate(n):
            if (current_value + v) // 10 > 4:
                is_09 = True
                break
            if (current_value + v) // 10 == 4:
                is_weapon = True
                break
            if (current_value + v) // 10 != current_value // 10:
                answer += (current_value + v) // 10
            current_value += v
        answers[i] = f"{answer}{'(weapon)' if is_weapon else ''}{'(09)' if is_09 else ''}"
    print(answers)