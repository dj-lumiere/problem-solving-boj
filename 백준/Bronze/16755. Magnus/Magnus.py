import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for a in range(t):
        word = list(input().decode())
        target = "HONI"
        match = 0
        for i, v in enumerate(word):
            if v == target[match % 4]:
                match += 1
        answer = match // 4
        answers[a] = f"{answer}"
    print(answers)