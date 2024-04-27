import os

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
        n, t1, t2, t3 = [int(input()) for _ in range(4)]
        if n == t1 == t2 == t3 == 0:
            break
        answer = []
        for i in range(n):
            answer_sub = n * 3 + (t1-i)%n + (t2 - t1) % n + (t2 - t3) % n
            answer.append(answer_sub)
        answers.append(f"{max(answer)}")
    print(answers)