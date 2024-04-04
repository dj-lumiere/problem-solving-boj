import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    answers = ["" for _ in range(t)]
    for i in range(t):
        c, v = int(next(tokens)), int(next(tokens))
        you_piece, dad_piece = divmod(c, v)
        answers[i] = f"You get {you_piece} piece(s) and your dad gets {dad_piece} piece(s)."
    os.write(1, "\n".join(answers).encode())