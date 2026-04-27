import os
from collections import Counter

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
        books = [input().decode() for _ in range(n)]
        answer = Counter(books).most_common()
        answer.sort(key=lambda x:(-x[1], x[0]))
        answers[i] = f"{answer[0][0]}"
    print(answers)