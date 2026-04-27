import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    first_prize = [0] + [5_000_000] * 1 + [3_000_000] * 2 + [2_000_000] * 3 + [500_000] * 4 + [300_000] * 5 + [
        100_000] * 6 + [0] * 100
    second_prize = [0] + [5_120_000] * 1 + [2_560_000] * 2 + [1_280_000] * 4 + [640_000] * 8 + [320_000] * 16 + [0] * 64
    answers = ["" for _ in range(t)]
    for i in range(t):
        a, b = int(next(tokens)), int(next(tokens))
        answers[i] = str(first_prize[a] + second_prize[b])
    os.write(1, "\n".join(answers).encode())