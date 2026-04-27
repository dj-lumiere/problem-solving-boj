import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        g, s, c = [int(input()) for _ in range(3)]
        answer = []
        if g * 3 + s * 2 + c >= 8:
            answer.append("Province")
        elif g * 3 + s * 2 + c >= 5:
            answer.append("Duchy")
        elif g * 3 + s * 2 + c >= 2:
            answer.append("Estate")
        if g * 3 + s * 2 + c >= 6:
            answer.append("Gold")
        elif g * 3 + s * 2 + c >= 3:
            answer.append("Silver")
        elif g * 3 + s * 2 + c >= 0:
            answer.append("Copper")
        answer = " or ".join(answer)
        answers[h] = f"{answer}"
    print(answers)