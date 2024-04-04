import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        h, w = int(input()), int(input())
        grid = [list(input()) for _ in range(h)]
        horizontal_filled = [any(a == ord("X") for a in grid[b]) for b in range(h)]
        vertical_filled = [any(a == ord("X") for a in [grid[b][c] for b in range(h)]) for c in range(w)]
        answers[i] = str(max(h - sum(horizontal_filled), w - sum(vertical_filled)))
    print(answers)