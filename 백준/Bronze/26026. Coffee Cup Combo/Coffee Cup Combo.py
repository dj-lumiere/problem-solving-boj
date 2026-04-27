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
        classes = list(map(int, input().decode()))
        coffees = classes[:]
        for j, v in enumerate(classes):
            if v == 1:
                if j + 1 < n:
                    coffees[j + 1] = 1
                if j + 2 < n:
                    coffees[j + 2] = 1
        answers[i] = f"{sum(coffees)}"
    print(answers)