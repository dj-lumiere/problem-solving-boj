import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = input().decode()
        if "-" in n:
            x = list(range(2000, 2020)) + list(range(1920, 2000))
            answer = str(x[int(n[:2])]) + n[2:6] + n[7:]
        else:
            x = list(range(1900, 1920)) + list(range(1820, 1900))
            answer = str(x[int(n[:2])]) + n[2:6] + n[7:]
        answers[h] = f"{answer}"
    print(answers)