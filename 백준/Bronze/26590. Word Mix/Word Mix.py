import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        n = input().decode()
        m = input().decode()
        answer = [n[i] if i % 2 == 0 else m[i] for i in range(min(len(n), len(m)))]
        answers[h] = "".join(answer)
    print(answers)