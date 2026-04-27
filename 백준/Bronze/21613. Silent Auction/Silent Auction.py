import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for a in range(t):
        n = int(input())
        current_max_name = ""
        current_max = 0
        for _ in range(n):
            name = input().decode()
            value = int(input())
            if value > current_max:
                current_max_name = name
                current_max = value
        answers[a] = current_max_name
    print(answers)