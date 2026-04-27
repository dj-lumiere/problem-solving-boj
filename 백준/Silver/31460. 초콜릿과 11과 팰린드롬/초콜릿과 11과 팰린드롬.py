import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
t = int(next(tokens))
answers = ["" for _ in range(t)]
for i in range(t):
    n = int(next(tokens))
    if n % 4 == 3:
        answers[i] = "1" * (n // 2) + "2" + "1" * (n // 2)
    elif n % 4 == 1:
        answers[i] = "1" * (n // 2) + "0" + "1" * (n // 2)
    else:
        answers[i] = "1" * n
os.write(1, "\n".join(answers).encode())
