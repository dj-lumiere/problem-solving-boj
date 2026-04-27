import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
t = int(next(tokens))
answers = ["" for _ in range(t)]
for i in range(t):
    expr = next(tokens)
    number_point = -1
    for j, v in enumerate(expr):
        if ord("0") <= v <= ord("1"):
            number_point = j
            break
    n = expr[number_point] - ord("0")
    before_factorial = number_point
    after_factorial = len(expr) - number_point - 1
    answer = 1 if after_factorial or n == 1 else 0
    if before_factorial % 2:
        answer ^= 1
    answers[i] = str(answer)
os.write(1, "\n".join(answers).encode())
