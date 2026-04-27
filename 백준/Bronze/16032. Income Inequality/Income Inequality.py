import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    for i in range(t):
        pass
    while True:
        n = int(input())
        if n == 0:
            break
        incomes = [int(input()) for _ in range(n)]
        average = sum(incomes) // n
        answers.append(f"{sum(i <= average for i in incomes)}")
    print(answers)