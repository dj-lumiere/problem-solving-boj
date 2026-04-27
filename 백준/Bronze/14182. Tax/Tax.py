import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        answer = n * 8 // 10 if n > 5000000 else n * 9 // 10 if n > 1000000 else n
        answers.append(f"{answer}")
    print(answers)