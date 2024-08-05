import os
from itertools import permutations
from math import factorial

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="": os.write(1, (sep.join(map(str, *args)) + end).encode())
    eprint = lambda *args, sep=" ", end="\n": os.write(2, (sep.join(map(str, *args)) + end).encode())
    t = 0
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        try:
            word = input().decode().strip()
            n = int(input()) - 1
            if n >= factorial(len(word)):
                answer = f"{word} {n + 1} = No permutation"
            else:
                target = []
                for i, group in enumerate(permutations(word)):
                    if i == n:
                        target = group
                        break
                answer = f"{word} {n + 1} = {''.join(target)}"
            answers.append(answer)
        except StopIteration:
            break
    print(answers)