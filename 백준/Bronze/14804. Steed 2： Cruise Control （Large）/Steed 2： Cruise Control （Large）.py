import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        d = int(input())
        n = int(input())
        horses = []
        for _ in range(n):
            k, s = int(input()), int(input())
            horses.append((d - k) / s)
        answer = d / max(horses)
        answers[i] = f"Case #{i + 1}: {answer}"
    print(answers)