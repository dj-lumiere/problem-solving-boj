import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = next(tokens)
        if (int(n[-1]) - ord("0")) % 2:
            answers[i] = "odd"
        else:
            answers[i] = "even"
    os.write(1, "\n".join(answers).encode())