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
        balloons = list(input().decode())
        a_count = sum(i == "a" for i in balloons)
        b_count = sum(i == "b" for i in balloons)
        answers[i] = f"{min(a_count, b_count)}"
    print(answers)