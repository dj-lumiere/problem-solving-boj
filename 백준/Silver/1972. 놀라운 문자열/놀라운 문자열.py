import os
from collections import Counter
from itertools import product
from array import array
from functools import reduce

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        word = input().decode().strip()
        if word == "*":
            break
        is_answer = True
        for i in range(1, len(word)):
            substring = []
            for j in range(len(word) - i):
                substring.append(word[j] + word[j + i])
            substring_count = Counter(substring)
            for j, v in substring_count.items():
                if v > 1:
                    is_answer = False
                    break
            if not is_answer:
                break
        answer = f"{word} {'is NOT' if not is_answer else 'is'} surprising."
        answers.append(f"{answer}")
    print(answers)