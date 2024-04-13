import os
import datetime

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        n = int(input())
        word = input().decode()
        answer = False
        for i in range(n):
            is_answer = False
            if i + 4 >= n:
                continue
            for j in range(4):
                if abs(ord(word[i + j]) - ord(word[i + j + 1])) != 1:
                    break
            else:
                is_answer = True
            if is_answer:
                answer = True
        answers[h] = "YES" if answer else "NO"
    print(answers)