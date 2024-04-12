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
        digits = len(str(n))
        yugene_number = False
        for j in range(1, digits):
            x, y = divmod(n, 10 ** j)
            x_mul, y_mul = 1, 1
            for v in map(int, str(x)):
                x_mul *= v
            for v in map(int, "0" * (j - len(str(y))) + str(y)):
                y_mul *= v
            if x_mul == y_mul:
                yugene_number = True
                break
        answers[i] = f"{'YES' if yugene_number else 'NO'}"
    print(answers)