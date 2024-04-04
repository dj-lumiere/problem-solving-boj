import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        current_max = 0
        current_school = ""
        for j in range(n):
            s, l = input().decode(), int(input())
            if l > current_max:
                current_school = s
                current_max = l
        answers[i] = str(current_school)
    os.write(1, "\n".join(answers).encode())