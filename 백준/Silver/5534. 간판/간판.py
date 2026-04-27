import os
from collections import Counter
from itertools import combinations, product
from array import array
from functools import reduce

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
        target = input().decode()
        words = [input().decode()+" "*10000 for _ in range(n)]
        answer = 0
        for word in words:
            found_answer = False
            for i in range(100):
                for j in range(1, 100):
                    if target == word[i:i+len(target)*j:j]:
                        answer += 1
                        found_answer = True
                        break
                if found_answer:
                    break
        answers[h] = f"{answer}"
    print(answers)