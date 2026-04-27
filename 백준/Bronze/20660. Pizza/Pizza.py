import os
from itertools import permutations

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
        a = [int(input()) for _ in range(n)]
        m = int(input())
        toppings = [set() for _ in range(m)]
        for j in range(m):
            topping_count = int(input())
            for _ in range(topping_count):
                toppings[j].add(int(input()))
        answer = 0
        for topping in toppings:
            if any(j in topping for j in a):
                continue
            answer += 1
        answers[i] = str(answer)
    print(answers)