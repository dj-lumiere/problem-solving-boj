import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(next(tokens))
        total_c = 0
        total_score = 0
        for _ in range(n):
            c, g = int(next(tokens)), int(float(next(tokens)) * 10)
            total_c += c
            total_score += c * g
        answers[i] = f"{total_c} {total_score / total_c / 10:.1f}"
    os.write(1, "\n".join(answers).encode())