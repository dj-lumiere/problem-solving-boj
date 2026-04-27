import os
from collections import Counter

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        m = int(input())
        problem_type = input().decode()
        task = []
        if problem_type == "C":
            task = [input().decode() for _ in range(m)]
        elif problem_type == "N":
            task = [int(input()) for _ in range(m)]
        answer = []
        if problem_type == "C":
            answer = [ord(j) - ord("A") + 1 for j in task]
        elif problem_type == "N":
            answer = [chr(ord("A") + j - 1) for j in task]
        answers[i] = " ".join(map(str, answer))
    print(answers)