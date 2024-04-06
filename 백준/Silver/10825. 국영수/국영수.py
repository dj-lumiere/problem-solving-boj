import os

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
        students = [(input().decode(), int(input()), int(input()), int(input())) for _ in range(n)]
        students.sort(key=lambda x:(-x[1], x[2], -x[3],x[0]))
        answer = "\n".join(map(lambda x:x[0], students))
        answers[i] = f"{answer}"
    print(answers)
